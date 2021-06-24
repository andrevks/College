package apps;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Excluir1 {
    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;
        int codigo = Integer.parseInt(
                JOptionPane.showInputDialog("Forneca o codigo do grupo de produto a ser excluido")
        );

        try {
            comando = conexao.prepareStatement("DELETE FROM grupoproduto WHERE codigo=?");
            comando.setInt(1, codigo);
            int contRec = comando.executeUpdate();
            if (contRec == 1){
                System.out.println("Exclusao realizada com sucesso [ " + contRec + " excluido]");
            }else {
                System.out.println("Exclusao NAO realizada ");
            }
        }catch (SQLException ex){
            System.out.println("Erro ao excluir o grupo de produto" + ex.toString());
        } finally {
            try{
                comando.close();
                conexao.close();
            }catch (SQLException ex){
                System.out.println("Erro ao desconectar " + ex.toString());
            }
        }
    }
}
