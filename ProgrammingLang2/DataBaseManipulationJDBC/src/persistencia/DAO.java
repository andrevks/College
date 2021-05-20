package persistencia;

/*
Superclasse para as classes de persistência (DAO).

*/

public class DAO {

    protected ConexaoDB conexao;

    public DAO(ConexaoDB conexao) throws PersistenciaException{
        this.conexao = conexao;
    }

    public ConexaoDB getConexao() {
        return conexao;
    }

    public void setConexao(ConexaoDB conexao) {
        this.conexao = conexao;
    }

    public  void desconectarBD() throws PersistenciaException{
        conexao.desconectar();
    }
}
