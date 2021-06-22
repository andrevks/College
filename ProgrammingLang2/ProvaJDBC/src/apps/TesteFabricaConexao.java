package apps;

import java.sql.Connection;
import java.sql.SQLException;

public class TesteFabricaConexao {

    public static void main(String[] args) {
        Connection conexao;
        try{
            conexao = FabricaConexao.obterConexao();
            System.out.println("Conexao estabelecida");
            conexao.close();
            System.out.println("Conexao encerrada");
        }catch (SQLException sqle){
            System.out.println("Banco nao estabelecida - " + sqle.getMessage());
        }
    }
}