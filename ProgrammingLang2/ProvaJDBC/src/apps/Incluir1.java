package apps;

import javax.swing.*;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class Incluir1 {

    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        Statement comando = null;
        String nome = JOptionPane.showInputDialog("Forneca o nome do grupo de produto");
        float promocao = Float.parseFloat(JOptionPane.showInputDialog("Forneca" +
                " o percentual de promocao do grupo de produto"));
        float margem = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percetual" +
                " da margem de lucro do grupo de produto"));
        String sql = "INSERT INTO grupoproduto(nome, promocao, margemlucro) VALUES " +
                "('" + nome + "', " + promocao + ", " + margem + ")";

        try {
            comando = conexao.createStatement();
            comando.executeUpdate(sql);
            System.out.println("Inclusao realizada com sucesso");
        }catch (SQLException ex){
            System.out.println("Erro ao incluir grupo de produto" + ex.toString());
        }finally {
            try {
                comando.close();
                conexao.close();
            }catch (SQLException ex) {
                System.out.println("Erro ao desconectar" + ex.toString());
            }
        }
    }
}
