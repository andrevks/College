package apps;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class ContextoPersistencia {

    public static void main(String[] args) {

        EntityManagerFactory emf = null;
        EntityManager em = null;

        try {
            emf = Persistence.createEntityManagerFactory("UnidadeBDPostgre");
            em = emf.createEntityManager();
            System.out.println("Contexto de persistencia criado com sucesso");
        }catch (Exception ex){
            System.out.println(ex.toString());
            System.out.println("Contexto de persistencia nao foi criado - " + ex.getMessage());
        }finally {
            if(em != null)
                em.close();

            if(emf != null)
                emf.close();
        }
    }
}
