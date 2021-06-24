package apps;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Alterar1 {
    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;

        int codigo = Integer.parseInt(
                JOptionPane.showInputDialog("Forneca o codigo do grupo de produto a ser alterado")
        );
        float promocao = Float.parseFloat(
                JOptionPane.showInputDialog("Forneca o percentual de promocao ")
        );
        float margem = Float.parseFloat(
                JOptionPane.showInputDialog("Forneca o percentual da marguem de lucro")
        );

        try {
            comando = conexao.prepareStatement("UPDATE grupoproduto SET promocao=?, margemlucro=? WHERE" +
                    "   codigo=?");
            comando.setFloat(1,promocao);
            comando.setFloat(2, margem);
            comando.setInt(3,codigo);
            int contRec = comando.executeUpdate();
            System.out.println("Alteracao realizada com sucesso");
            System.out.println("Numero de registros alterados: " + contRec);
        }catch (SQLException ex){
            System.out.println("Erro ao alterar o grupo " + ex.toString());
        }finally {
            try {
                comando.close();
                conexao.close();
            }catch (SQLException ex){
                System.out.println("Erro ao desconectar" + ex.toString());
            }
        }
    }
}
