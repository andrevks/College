package persistencia;

import vo.CursoVO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/*
   (inclusão, alteração, exclusão, busca por codigo e busca por nome)
 */
public class CursoDAO extends DAO{

    private static PreparedStatement comandoIncluir;
    private static PreparedStatement comandoAlterar;
    private static PreparedStatement comandoExcluir;
    private static PreparedStatement comandoBuscaCodigo;

    public CursoDAO(ConexaoBD conexao) throws PersistenciaException {
        super(conexao);
        try{
            comandoIncluir = conexao.getConexao().prepareStatement("INSERT INTO curso(nome,descricao)" +
                    "VALUES(?,?)");
            comandoAlterar = conexao.getConexao().prepareStatement("UPDATE curso SET nome=?, descricao=? WHERE codigo=?");
            comandoExcluir = conexao.getConexao().prepareStatement("DELETE FROM curso WHERE codigo=?");
            comandoBuscaCodigo = conexao.getConexao().prepareStatement("SELECT * FROM curso WHERE" +
                    " codigo=?");
        }catch (SQLException ex){
            throw new PersistenciaException("CursoDAO: Erro ao incluir novo curso - " + ex.getMessage());
        }
    }

    public int incluir(CursoVO cursoVO) throws PersistenciaException{
        int retorno = 0;
        try {
            comandoIncluir.setString(1,cursoVO.getNome());
            comandoIncluir.setString(2,cursoVO.getDescricao());
            retorno = comandoIncluir.executeUpdate();
        } catch (SQLException ex) {
            throw new PersistenciaException("Erro ao incluir curso - " + ex.getMessage());
        }
        return retorno;
    }

    public int alterar(CursoVO cursoVO)throws PersistenciaException{
        int retorno = 0;
        try {
            comandoAlterar.setString(1,cursoVO.getNome());
            comandoAlterar.setString(2,cursoVO.getDescricao());
            comandoAlterar.setInt(3,cursoVO.getCodigo());
            retorno = comandoAlterar.executeUpdate();
        }catch (SQLException ex){
            throw new PersistenciaException("Erro ao alterar o curso - " + ex.getMessage());
        }
        return retorno;
    }

    public int excluir(int codigo) throws PersistenciaException {
        int retorno = 0;
        try {
            comandoExcluir.setInt(1,codigo);
            retorno = comandoExcluir.executeUpdate();
        }catch (SQLException ex){
            throw new PersistenciaException("Erro ao excluir o curso - " + ex.getMessage());
        }
        return retorno;
    }

    public CursoVO buscarPorCodigo(int codigo) throws PersistenciaException {
        CursoVO curso = null;

        try {
            comandoBuscaCodigo.setInt(1,codigo);
            ResultSet rs = comandoBuscaCodigo.executeQuery();
            if(rs.next()){
                curso = this.montaCursoVO(rs);
            }
        } catch (SQLException ex) {
            throw new PersistenciaException("Erro na selecao por codigo - " + ex.getMessage());
        }
        return curso;
    }

    public List<CursoVO> buscarPorNome(String nome) throws PersistenciaException {
        List<CursoVO> listaCurso = new ArrayList<>();
        CursoVO curso = null;

        String comandoSQL = "SELECT * FROM curso WHERE UPPER(nome) LIKE'"+nome.trim().toUpperCase() +
                "%' ORDER BY NOME LIMIT 10";

        try {
            PreparedStatement comando = conexao.getConexao().prepareStatement(comandoSQL);
            ResultSet rs = comando.executeQuery();
            while(rs.next()){
                curso = this.montaCursoVO(rs);
                listaCurso.add(curso);
            }
            comando.close();
        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao por nome - " + ex.getMessage());
        }
        return listaCurso;
    }

    private CursoVO montaCursoVO(ResultSet rs) throws PersistenciaException {
        CursoVO curso = new CursoVO();
        if(rs != null){
            try {
                curso.setCodigo(rs.getInt("codigo"));
                curso.setNome(rs.getString("nome"));
                curso.setDescricao(rs.getString("descricao"));
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }
        return curso;
    }
}
