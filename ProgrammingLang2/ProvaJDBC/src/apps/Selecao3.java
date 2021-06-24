package apps;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Selecao3 {
    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;
        String nome = JOptionPane.showInputDialog("Forneca parte do nome a ser pesquisado");
        try{
            comando = conexao.prepareStatement("SELECT * FROM grupoproduto WHERE upper(nome) LIKE ? ");
            comando.setString(1, "%" + nome.toUpperCase() + "%");
            ResultSet resultado = comando.executeQuery();
            if (resultado.next()){
                do{
                    System.out.println("Codigo: " + resultado.getInt("codigo"));
                    System.out.println("Nome: " + resultado.getString("nome"));
                    System.out.println("Promocao: " + resultado.getDouble("promocao"));
                    System.out.println("Margem Lucro: " + resultado.getDouble("margemlucro"));
                    System.out.println("--------------------------------------------------------------");
                }while (comando.execute());
            }else{
                System.out.println("Nao encontrado! ");
            }
        }catch (SQLException ex){
            System.out.println("Erro ao recuperar um grupo " + ex.toString());
        }finally {
            try{
                comando.close();
                conexao.close();
            }catch (SQLException ex){
                System.out.println("Erro ao deconectar" + ex.toString());
            }
        }
    }
}
