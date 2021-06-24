package apps;

import javax.swing.*;
import java.sql.*;

public class Incluir3 {
    public static void main(String[] args) {
        Connection conexao = FabricaConexao.obterConexao();
        PreparedStatement comando = null;
        String nome = JOptionPane.showInputDialog("Forneca o nome do grupo de produto");
        float promocao = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual de promocao " +
                "do grupo de produto"));
        float margem = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual da marguem de lucro" +
                " do grupo de produto"));
        try {
            String sql = "INSERT INTO grupoproduto ( nome, promocao, margemlucro ) VALUES(?,?,?)";
            comando = conexao.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
            comando.setString(1, nome);
            comando.setFloat(2, promocao);
            comando.setFloat(3, margem);
            comando.executeUpdate();
            ResultSet rs = comando.getGeneratedKeys();
            long chave = 0;
            if(rs.next()){
                chave = rs.getLong("codigo");
            }
            System.out.println("Inclusao realizada com sucesso [chave: " + chave + "]");
        }catch (SQLException ex){
            System.out.println("Erro ao incluir grupo produto" + ex.toString());
        }finally {
            try{
                comando.close();
                conexao.close();
            }catch (SQLException ex){
                System.out.println("Erro ao desconectar " + ex.toString());
            }
        }
    }
}
