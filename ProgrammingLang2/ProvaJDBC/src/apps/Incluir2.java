package apps;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Incluir2{
    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;
        String nome = JOptionPane.showInputDialog("Forneca o nome do grupo de produto");
        float promocao = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual de promocao " +
                "do grupo de produto"));
        float margem = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual da marguem de lucro" +
                " do grupo de produto"));

        try {
            comando = conexao.prepareStatement("INSERT INTO grupoproduto ( nome, promocao, margemlucro )" +
                    "VALUES(?, ?, ?)");
            comando.setString(1, nome);
            comando.setFloat(2, promocao);
            comando.setFloat(3, margem);
            comando.executeUpdate();
            System.out.println("Inclusao realizada com sucesso");
        }catch (SQLException ex){
            System.out.println("Erro ao incluir grupo de produto" + ex.toString());
        }finally {
            try{
                comando.close();
                conexao.close();
            }catch (SQLException ex){
                System.out.println("Erro ao desconectar" + ex.toString());
            }
        }

    }
}
