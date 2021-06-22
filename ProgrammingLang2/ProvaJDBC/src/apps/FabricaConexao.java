package apps;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class FabricaConexao {
    //"static" = is shared with all the objects of the class.
    //"static final" = compile-time constant because it loads
    // in memory when a class loads to memory.
    private static final String URL = "jdbc:postgresql://localhost:5432/produto";
    private static final String DRIVE = "org.postgresql.Driver";
    private static final String USER = "postgres";
    private static final String PASS = "postgres";

    public static Connection obterConexao(){
        Connection conexao = null;

        try {
            Class.forName(DRIVE);
            conexao = DriverManager.getConnection(URL,USER, PASS);
        }catch (ClassNotFoundException cnf){
            System.out.println("Driver nao encontrado - " + cnf.getMessage());
        } catch (SQLException sqle) {
            System.out.println("Erro ao conectar no banco - " + sqle.getMessage());
        }
        return conexao;
    }


}
