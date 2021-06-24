package apps;

import org.jetbrains.annotations.NotNull;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

public class Incluir4 {
    private static final Connection CONEXAO;

    static {
        CONEXAO = FabricaConexao.obterConexao();
    }

    public static void main(String[] args) {
        PreparedStatement comando = null;
        Map<String, Integer> listaGrupos = obterGruposProdutos();

        String nome = JOptionPane.showInputDialog("Forneca o nome do produto");
        int estoque = Integer.parseInt(JOptionPane.showInputDialog("Forneca a quantidade em estoque do produto"));
        float valorCompra = Float.parseFloat(JOptionPane.showInputDialog("Forneca o valor de compra do produto"));
        float promocao = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual de promocao " +
                "do produto"));
        float margem = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual da marguem de lucro" +
                " do produto"));
        String nomeGrupo = (String) JOptionPane.showInputDialog(null,
                                                                "Escolha o grupo de produto",
                                                                "Grupos de produto",
                                                                 JOptionPane.QUESTION_MESSAGE,
                                                                  null,
                                                                   listaGrupos.keySet().toArray(),
                                                                   listaGrupos.keySet().toArray()[0]);
        try {
            comando = CONEXAO.prepareStatement("INSERT INTO produto (nome, estoque, valorcompra, promocao," +
                    " margemlucro, grupo) VALUES(?, ?, ?, ?, ?, ?");
            comando.setString(1,nome);
            comando.setInt(2,estoque);
            comando.setFloat(3,valorCompra);
            comando.setFloat(4,promocao);
            comando.setFloat(5,margem);
            comando.setInt(6,listaGrupos.get(nomeGrupo));
            comando.executeUpdate();
            System.out.println("Inclusao do produto realizada com sucesso");
        }catch (SQLException ex){
            System.out.println("Erro ao incluir produto " + ex.toString());
        }finally {
            try {
                comando.close();
                CONEXAO.close();
            }catch (SQLException ex){
                System.out.println("Erro ao desconectar " + ex.toString());
            }
        }
    }

    public static Map<String, Integer> obterGruposProdutos(){
        Map<String, Integer> listaGrupos = new HashMap();

        PreparedStatement comando = null;
        try{
            comando = CONEXAO.prepareStatement("SELECT * FROM grupoproduto " +
                    "ORDER BY nome");
            ResultSet resultado = comando.executeQuery();
            while (resultado.next()){
                listaGrupos.put(
                        resultado.getString("nome"),
                        resultado.getInt("codigo")
                );
            }
            resultado.close();
        }catch (SQLException ex){
            System.out.println("Erro ao recuperar os grupos de produtos" + ex.toString());
        }finally {
            try {
                comando.close();
            }catch (SQLException ex){
                System.out.println("Erro ao desconectar " + ex.toString());
            }
        }
        System.out.println(listaGrupos);
        return listaGrupos;
    }
}
