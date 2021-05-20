package persistencia;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/*
* Classe responsável por criar e retornar uma instância de conexão com o banco de dados.
 *  */
public class ConexaoBD {

    private Connection con;
    private static ConexaoDB instancia;

    private ConexaoDB() throws  PersistenciaException {
        try {
            Class.forName("org.postgresql.Driver");
            String url = "jdbc:postgresql://localhost:5432/academico";
            con = DriverManager.getConnection(url,"postgres","postgres");
        } catch (SQLException ex){
            throw new PersistenciaException("Erro ao conectar ao banco de dados - " +
                    ex.toString());
        } catch (ClassNotFoundException ex){
            throw new PersistenciaException("Driver do banco de dados nao localizado - " +
                    ex.toString());
        }
    }

    public Connection getConexao() {
        return con;
    }

    public void desconectar() throws PersistenciaException {
        try {
            con.close();
        }catch (SQLException ex){
            throw new PersistenciaException("Erro ao desconectar o banco de dados - " +
                    ex.toString());
        }
    }

}
