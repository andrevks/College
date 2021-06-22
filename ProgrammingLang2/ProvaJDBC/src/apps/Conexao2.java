package apps;

import org.postgresql.Driver;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexao2 {

    public static void main(String[] args) {
        Connection conexao;
        String url = "jdbc:postgresql://localhost:5432/produto";
        String usr = "postgres";
        String pass = "postgres";
        try {
            DriverManager.registerDriver(new Driver());//Only difference
            conexao = DriverManager.getConnection(url,usr,pass);
            System.out.println("Conexao estabelecida");
            conexao.close();
            System.out.println("Conexao encerrada");
        }catch (SQLException sqle){
            System.out.println("Conexao nao estabelecida - " + sqle.getMessage());
        }
    }
}
