package apps;

import vo.GrupoProdutoVO;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;
import javax.swing.*;
import java.util.List;

public class Alterar1 {

    public static void main(String[] args) {
        EntityManagerFactory emf = null;
        EntityManager em = null;
        GrupoProdutoVO grupoVO = null;

        try {
            emf = Persistence.createEntityManagerFactory("UnidadeBDPostgre");
            em = emf.createEntityManager();
            em.getTransaction().begin();
            String pNome = JOptionPane.showInputDialog("Forneca o nome do grupo de produto a ser localizado");

            Query consulta = em.createQuery("SELECT gp FROM GrupoProdutoVO gp WHERE UPPER(gp.nome) = :pNome ");
            consulta.setParameter("pNome", pNome.toUpperCase());
            List<GrupoProdutoVO> lista = consulta.getResultList();
            if(lista.size() > 0){
                grupoVO = lista.get(0);
                String nome = JOptionPane.showInputDialog("Forneca o nome do grupo de produto");
                float margem = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual da margem de" +
                        " lucro do grupo de produto"));
                float promocao = Float.parseFloat(JOptionPane.showInputDialog("Forneca o percentual de promocao " +
                        "do grupo de produto"));
                grupoVO.setNome(nome);
                grupoVO.setMargemLucro(margem);
                grupoVO.setPromocao(promocao);
                em.merge(grupoVO);
                em.getTransaction().commit();
                System.out.println("Alteracao realizada com sucesso");
            }
        }catch (Exception ex){
            System.out.println("Alteracao nao realizada - " + ex.getMessage());
        }finally {
            if(em != null)
                em.close();

            if(emf != null)
                emf.close();
        }
    }
}
