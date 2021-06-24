package apps;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Selecao2 {

    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;
        int codigo = Integer.parseInt(JOptionPane.showInputDialog("Forneca o codigo a ser pesquisado"));
        try {
            comando = conexao.prepareStatement("SELECT * FROM grupoproduto WHERE codigo=?");
            comando.setInt(1,codigo);
            ResultSet resultado = comando.executeQuery();
            if(resultado.next()){
                System.out.println("Encontrado: " + resultado.getString("nome"));
            }else {
                System.out.println("Nao encontrado! ");
            }
        } catch (SQLException ex){
            System.out.println("Erro ao recuperar um grupo " + ex.toString());
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
