package apps;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Selecao1 {
    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;
        try{
            comando = conexao.prepareStatement("SELECT * FROM grupoproduto ORDER" +
                    " BY nome");
            ResultSet resultado = comando.executeQuery();
            while(resultado.next()){
                System.out.println("Codigo: " + resultado.getInt("codigo"));
                System.out.println("Nome: " + resultado.getString("nome"));
                System.out.println("Promocao: " + resultado.getDouble("promocao"));
                System.out.println("Margem Lucro: " + resultado.getDouble("margemlucro"));
                System.out.println("--------------------------------------------------------------");
            }
            resultado.close();
        }catch (SQLException ex){
            System.out.println("Erro ao recuperar os grupos de produtos" + ex.toString());
        }finally {
            try {
                comando.close();
                conexao.close();
            } catch (SQLException ex) {
                System.out.println("Erro ao desconectar" + ex.toString());
            }
        }
    }
}
