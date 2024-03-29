package vo;

import java.io.Serializable;
import javax.persistence.Table;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
@Table(name = "grupoproduto")
public class GrupoProdutoVO implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private int codigo;
    private String nome;
    private float margemLucro;
    private float promocao;

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public float getMargemLucro() {
        return margemLucro;
    }

    public void setMargemLucro(float margemLucro) {
        this.margemLucro = margemLucro;
    }

    public float getPromocao() {
        return promocao;
    }

    public void setPromocao(float promocao) {
        this.promocao = promocao;
    }

    @Override
    public String toString(){
        return this.nome + " - " + this.codigo;
    }

    @Override
    public boolean equals(Object obj){
        if(obj == null){
            return false;
        }
        if(getClass() != obj.getClass()){
            return false;
        }
        final GrupoProdutoVO other = (GrupoProdutoVO) obj;
        if(this.codigo != other.codigo){
            return false;
        }
        return true;
    }
}
