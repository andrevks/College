package apps;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class Conexao3 {
    public static void main(String[] args) {

        Properties proBD = new Properties();
        FileInputStream leitorArquivo;
        try {
            leitorArquivo = new FileInputStream("apps/conexao.properties");
            proBD.load(leitorArquivo);
            leitorArquivo.close();
        }catch (FileNotFoundException ex){
            System.out.println("Arquivo de configuracoes nao encontrado - " + ex.getMessage());
        }catch (IOException ex){
            System.out.println("Erro ao ler o arquivo de configuracoes - " + ex.getMessage());
        }

        if(!proBD.isEmpty()){
            Connection conexao;
            String url = proBD.getProperty("url");
            String driver = proBD.getProperty("driver");
            String usr = proBD.getProperty("usuario");
            String pass = proBD.getProperty("senha");
            try {
                Class.forName(driver);
                conexao = DriverManager.getConnection(url, usr, pass);
                System.out.println("Conexao estabelecida");
                conexao.close();
                System.out.println("Conexao encerrada");
            }catch (ClassNotFoundException cnf){
                System.out.println("Driver nao encontrado - " + cnf.getMessage());
            } catch (SQLException sqle) {
                System.out.println("Banco nao encontrado - " + sqle.getMessage());
            }
        } else {
            System.out.println("Propriedades nao carregadas");
        }
    }
}
