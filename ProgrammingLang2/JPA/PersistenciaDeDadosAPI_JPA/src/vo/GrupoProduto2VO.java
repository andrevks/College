package vo;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "grupoproduto2")
public class GrupoProduto2VO implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private int codigo;

    @Column(length = 50, nullable = false)
    private String nome;

    @Column(precision = 5, scale = 2, nullable = false)
    private float margemLucro;

    @Column(precision = 5,scale = 2, nullable = false)
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
        return this.nome + " - "  + this.codigo;
    }

    @Override
    public boolean equals(Object obj){
        if(obj == null){
            return false;
        }
        if(getClass() != obj.getClass()){
            return false;
        }

        final GrupoProduto2VO other = (GrupoProduto2VO) obj;
        if(this.codigo != other.codigo){
            return false;
        }
        return true;
    }
}
