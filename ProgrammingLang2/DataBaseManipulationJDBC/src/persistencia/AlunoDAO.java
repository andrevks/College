package persistencia;

import vo.AlunoVO;
import vo.EnumSexo;
import vo.EnumUF;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/*
Subclasse de DAO, especializada nas operações de persistência para a entidade Aluno.
 */
public class AlunoDAO extends DAO{

    private static PreparedStatement comandoIncluir;
    private static PreparedStatement comandoAlterar;
    private static PreparedStatement comandoExcluir;
    private static PreparedStatement comandoBuscaMatricula;
    private static PreparedStatement comandoListarPorCurso;


    public AlunoDAO(ConexaoBD conexao) throws PersistenciaException{
        super(conexao);
        try{
            comandoIncluir = conexao.getConexao().prepareStatement("INSERT INTO Aluno" +
                    "( nome, nomemae, nomepai, sexo, logradouro, numero, bairro, cidade," +
                    "uf, curso)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
            comandoAlterar = conexao.getConexao().prepareStatement("UPDATE Aluno SET  nome=?, " +
                            "nomemae=?, nomepai=?, sexo=?, logradouro=?, numero=?, bairro=?, cidade=?," +
                            "uf=?, curso=? WHERE matricula=?");
            comandoExcluir = conexao.getConexao().prepareStatement("DELETE FROM Aluno WHERE" +
                    " matricula=?");
            comandoBuscaMatricula = conexao.getConexao().prepareStatement("SELECT * FROM Aluno WHERE matricula=?");
            comandoListarPorCurso = conexao.getConexao().prepareStatement("SELECT matricula, nome FROM Aluno WHERE curso=?");
        } catch (SQLException ex) {
           throw new PersistenciaException("Erro ao incluir novo aluno - " + ex.getMessage());
        }
    }

    public int incluir(AlunoVO alunoVO) throws PersistenciaException{
        int retorno = 0;
        try {
            comandoIncluir.setString(1,alunoVO.getNome());
            comandoIncluir.setString(2,alunoVO.getNomeMae());
            comandoIncluir.setString(3,alunoVO.getNomePai());
            comandoIncluir.setInt(4,alunoVO.getSexo().ordinal());
            comandoIncluir.setString(5,alunoVO.getEndereco().getLogradouro());
            comandoIncluir.setInt(6,alunoVO.getEndereco().getNumero());
            comandoIncluir.setString(7,alunoVO.getEndereco().getBairro());
            comandoIncluir.setString(8,alunoVO.getEndereco().getCidade());
            comandoIncluir.setString(9,alunoVO.getEndereco().getUf().name());
            comandoIncluir.setInt(10,alunoVO.getCurso());
            retorno = comandoIncluir.executeUpdate();
        } catch (SQLException ex) {
            throw new PersistenciaException("Erro ao incluir aluno - " + ex.getMessage());
        }
        return retorno;
    }
    public int alterar(AlunoVO alunoVO) throws PersistenciaException{
        int retorno = 0;
        try {
            comandoAlterar.setString(1,alunoVO.getNome());
            comandoAlterar.setString(2,alunoVO.getNomeMae());
            comandoAlterar.setString(3,alunoVO.getNomePai());
            comandoAlterar.setInt(4,alunoVO.getSexo().ordinal());
            comandoAlterar.setString(5,alunoVO.getEndereco().getLogradouro());
            comandoAlterar.setInt(6, alunoVO.getEndereco().getNumero());
            comandoAlterar.setString(7, alunoVO.getEndereco().getBairro());
            comandoAlterar.setString(8,alunoVO.getEndereco().getCidade());
            comandoAlterar.setString(9,alunoVO.getEndereco().getUf().name());
            comandoAlterar.setInt(10,alunoVO.getCurso());
            comandoAlterar.setInt(11, alunoVO.getMatricula());
            retorno = comandoAlterar.executeUpdate();
        } catch (SQLException ex) {
            throw new PersistenciaException("Erro ao alterar aluno - " + ex.getMessage());
        }
        return retorno;
    }

    public int excluir(int matricula) throws PersistenciaException {
        int retorno = 0;
        try {
            comandoExcluir.setInt(1,matricula);
            retorno = comandoExcluir.executeUpdate();
        }catch (SQLException ex){
            throw new PersistenciaException("Erro ao excluir aluno - " + ex.getMessage());
        }
        return retorno;
    }

    public AlunoVO buscarPorMatricula(int matricula) throws PersistenciaException {
        AlunoVO alu = null;

        try {
            comandoBuscaMatricula.setInt(1, matricula);
            ResultSet rs = comandoBuscaMatricula.executeQuery();
            if (rs.next()) {
                alu = this.montaAlunoVO(rs);
            }
        }catch(Exception ex){
                throw new PersistenciaException("Erro na selecao por codigo - " + ex.getMessage());
        }
        return alu;
    }

    public List<AlunoVO> buscarPorNome(String nome) throws PersistenciaException {
        List<AlunoVO> listaAluno = new ArrayList<>();
        AlunoVO alu = null;

        String comandoSQL = "SELECT * FROM Aluno WHERE UPPER(nome) LIKE '"
                +nome.trim().toUpperCase() + "%' ORDER BY NOME LIMIT 10";

        try {
            PreparedStatement comando = conexao.getConexao().prepareStatement(comandoSQL);
            ResultSet rs = comando.executeQuery();
            while(rs.next()){
                alu = this.montaAlunoVO(rs);
                listaAluno.add(alu);
            }
            comando.close();
        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao por nome - " + ex.getMessage());
        }
        return listaAluno;
    }
    private AlunoVO montaAlunoVO(ResultSet rs) throws PersistenciaException{
        AlunoVO alu = new AlunoVO();
        if(rs != null){
            try {
                alu.setMatricula(rs.getInt("matricula"));
                alu.setNome(rs.getString("nome"));
                alu.setNomeMae(rs.getString("nomemae"));
                alu.setNomePai(rs.getString("nomepai"));
                alu.setSexo(EnumSexo.values()[rs.getInt("sexo")]);
                alu.getEndereco().setLogradouro(rs.getString("logradouro"));
                alu.getEndereco().setNumero(rs.getInt("numero"));
                alu.getEndereco().setBairro(rs.getString("bairro"));
                alu.getEndereco().setCidade(rs.getString("cidade"));
                alu.getEndereco().setUf(EnumUF.valueOf(rs.getString("uf")));
                alu.setCurso(rs.getInt("curso"));
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }

        return alu;
    }

    private AlunoVO montaListaAlunoVO(ResultSet rs) throws PersistenciaException{
        AlunoVO alu = new AlunoVO();
        if(rs != null){
            try {
                alu.setMatricula(rs.getInt("matricula"));
                alu.setNome(rs.getString("nome"));
                alu.setSexo(EnumSexo.values()[rs.getInt("sexo")]);
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }

        return alu;
    }

    private AlunoVO montaListaAlunoPorCurso(ResultSet rs) throws PersistenciaException{
        AlunoVO alu = new AlunoVO();
        if(rs != null){
            try {
                alu.setMatricula(rs.getInt("matricula"));
                alu.setNome(rs.getString("nome"));
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }

        return alu;
    }

    public List<AlunoVO> listarAlunos() throws PersistenciaException{
        List<AlunoVO> listaAluno = new ArrayList<>();
        AlunoVO alu = null;

        String comandoSQL = "SELECT matricula, nome, sexo FROM Aluno";

        try{
           PreparedStatement comando = conexao.getConexao().prepareStatement(comandoSQL);
           ResultSet rs = comando.executeQuery();
           while(rs.next()){
               alu = this.montaListaAlunoVO(rs);
               listaAluno.add(alu);
           }

        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao dos alunos - " + ex.getMessage());
        }

        return listaAluno;
    }

    public List<AlunoVO> listarAlunos(int codigo) throws PersistenciaException{
        List<AlunoVO> listaAluno = new ArrayList<>();
        AlunoVO alu = null;

        try{
            comandoListarPorCurso.setInt(1,codigo);
            ResultSet rs = comandoListarPorCurso.executeQuery();
            while(rs.next()){
                alu = this.montaListaAlunoPorCurso(rs);
                listaAluno.add(alu);
            }

        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao dos alunos - " + ex.getMessage());
        }

        return listaAluno;
    }
}