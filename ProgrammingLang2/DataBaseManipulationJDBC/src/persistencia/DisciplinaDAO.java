package persistencia;

import vo.AlunoVO;
import vo.DisciplinaVO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class DisciplinaDAO extends DAO{

    private static PreparedStatement comandoIncluir;
    private static PreparedStatement comandoAlterar;
    private static PreparedStatement comandoExcluir;
    private static PreparedStatement comandoBuscaCodigo;
    private static PreparedStatement comandoListarPorCurso;

    public DisciplinaDAO(ConexaoBD conexao) throws PersistenciaException {
        super(conexao);
        try{
            comandoIncluir = conexao.getConexao().prepareStatement("INSERT INTO disciplina(nome, semestre, cargahoraria, " +
                    "curso)" +
                    "VALUES(?,?,?,?)");
            comandoAlterar = conexao.getConexao().prepareStatement("UPDATE disciplina SET nome=?, semestre=?, cargahoraria=?," +
                    "curso=? WHERE codigo=?");
            comandoExcluir = conexao.getConexao().prepareStatement("DELETE FROM disciplina WHERE codigo=?");
            comandoBuscaCodigo = conexao.getConexao().prepareStatement("SELECT * FROM disciplina WHERE" +
                    " codigo=?");
            comandoListarPorCurso =conexao.getConexao().prepareStatement("SELECT codigo, nome FROM disciplina WHERE curso=?") ;

        }catch (SQLException ex){
            throw new PersistenciaException("CursoDAO: Erro ao incluir nova disciplina - " + ex.getMessage());
        }
    }

    public int incluir(DisciplinaVO disciplinaVO) throws PersistenciaException{
        int retorno = 0;
        try {
            comandoIncluir.setString(1,disciplinaVO.getNome());
            comandoIncluir.setInt(2,disciplinaVO.getSemestre());
            comandoIncluir.setInt(3,disciplinaVO.getCargahoraria());
            comandoIncluir.setInt(4,disciplinaVO.getCurso());
            retorno = comandoIncluir.executeUpdate();
        } catch (SQLException ex) {
            throw new PersistenciaException("Erro ao incluir a disciplina - " + ex.getMessage());
        }
        return retorno;
    }

    public int alterar(DisciplinaVO disciplinaVO)throws PersistenciaException{
        int retorno = 0;
        try {
            comandoAlterar.setString(1,disciplinaVO.getNome());
            comandoAlterar.setInt(2,disciplinaVO.getSemestre());
            comandoAlterar.setInt(3,disciplinaVO.getCargahoraria());
            comandoAlterar.setInt(4,disciplinaVO.getCurso());
            comandoAlterar.setInt(5,disciplinaVO.getCodigo());
            retorno = comandoAlterar.executeUpdate();
        }catch (SQLException ex){
            throw new PersistenciaException("Erro ao alterar a disciplina - " + ex.getMessage());
        }
        return retorno;
    }

    public int excluir(int codigo) throws PersistenciaException {
        int retorno = 0;
        try {
            /*

            When you're using a relational DB, you are setting entities with relationships
             between these entities.

            The error that you're getting means that:

            You're trying to delete a record that its primary key is functioning as a foreign key
            in another table, thus you can't delete it.

            In order to delete that record, first, delete the record with the foreign key, and then delete
            the original that you wanted to delete.
             */
            comandoExcluir.setInt(1,codigo);
            retorno = comandoExcluir.executeUpdate();
        }catch (SQLException ex){
            throw new PersistenciaException("Erro ao excluir a disciplina - " + ex.getMessage());
        }
        return retorno;
    }

    public DisciplinaVO buscarPorCodigo(int codigo) throws PersistenciaException {
        DisciplinaVO disc = null;

        try {
            comandoBuscaCodigo.setInt(1,codigo);
            ResultSet rs = comandoBuscaCodigo.executeQuery();
            if(rs.next()){
                disc = this.montaDisciplinaVO(rs);
            }
        } catch (SQLException ex) {
            throw new PersistenciaException("Erro na selecao por codigo - " + ex.getMessage());
        }
        return disc;
    }

    public List<DisciplinaVO> buscarPorNome(String nome) throws PersistenciaException {
        List<DisciplinaVO> listaDisc = new ArrayList<>();
        DisciplinaVO disc = null;

        String comandoSQL = "SELECT * FROM disciplina WHERE UPPER(nome) LIKE'"+nome.trim().toUpperCase() +
                "%' ORDER BY NOME LIMIT 10";

        try {
            PreparedStatement comando = conexao.getConexao().prepareStatement(comandoSQL);
            ResultSet rs = comando.executeQuery();
            while(rs.next()){
                disc = this.montaDisciplinaVO(rs);
                listaDisc.add(disc);
            }
            comando.close();
        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao por nome - " + ex.getMessage());
        }
        return listaDisc;
    }

    private DisciplinaVO montaDisciplinaVO(ResultSet rs) throws PersistenciaException {
        DisciplinaVO disc = new DisciplinaVO();
        if(rs != null){
            try {
                disc.setCodigo(rs.getInt("codigo"));
                disc.setNome(rs.getString("nome"));
                disc.setSemestre(rs.getInt("semestre"));
                disc.setCargahoraria(rs.getInt("cargahoraria"));
                disc.setCurso(rs.getInt("curso"));
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }
        return disc;
    }

    private DisciplinaVO montaDisciplinas(ResultSet rs) throws PersistenciaException {
        DisciplinaVO disc = new DisciplinaVO();
        if(rs != null){
            try {
                disc.setCodigo(rs.getInt("codigo"));
                disc.setNome(rs.getString("nome"));
                disc.setSemestre(rs.getInt("semestre"));
                disc.setCargahoraria(rs.getInt("cargahoraria"));
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }
        return disc;
    }

    private DisciplinaVO montaDisciplinasPorCurso(ResultSet rs) throws PersistenciaException {
        DisciplinaVO disc = new DisciplinaVO();
        if(rs != null){
            try {
                disc.setCodigo(rs.getInt("codigo"));
                disc.setNome(rs.getString("nome"));
            }catch (Exception ex){
                throw new PersistenciaException("Erro ao acessar os dados do resultado");
            }
        }
        return disc;
    }

    public List<DisciplinaVO> listarDisciplinas() throws PersistenciaException {
        List<DisciplinaVO> listaDisc = new ArrayList<>();
        DisciplinaVO disc = null;

        String comandoSQL = "SELECT codigo, nome, semestre, cargahoraria FROM disciplina";

        try {
            PreparedStatement comando = conexao.getConexao().prepareStatement(comandoSQL);
            ResultSet rs = comando.executeQuery();
            while(rs.next()){
                disc = this.montaDisciplinas(rs);
                listaDisc.add(disc);
            }
            comando.close();
        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao por nome - " + ex.getMessage());
        }
        return listaDisc;


    }

    public List<DisciplinaVO> listarDisciplinasPorCurso(int codigo) throws PersistenciaException {
        List<DisciplinaVO> listaDisc = new ArrayList<>();
        DisciplinaVO disc = null;


        try {
            comandoListarPorCurso.setInt(1,codigo);
            ResultSet rs = comandoListarPorCurso.executeQuery();
            while(rs.next()){
                disc = this.montaDisciplinasPorCurso(rs);
                listaDisc.add(disc);
            }

        }catch (Exception ex){
            throw new PersistenciaException("Erro na selecao por nome - " + ex.getMessage());
        }
        return listaDisc;


    }
}
