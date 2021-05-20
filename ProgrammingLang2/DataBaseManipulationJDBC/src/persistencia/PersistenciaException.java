package persistencia;
/*
* Especialização da classe Exception para captura
* e tratamento de exceções ocorridas na camada de persitência.
*  */
public class PersistenciaException extends Exception{

    public PersistenciaException(){
        super("Erro ocorrido na manipulacao do banco de dados");
    }

    public PersistenciaException(String msg){
        super(msg);
    }
}
