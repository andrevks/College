package vo;

public class DisciplinaVO {
    private int codigo;
    private String nome;
    private String descricao;

    public CursoVO(){
        this.codigo = 0;
        this.nome = "";
        this.descricao = "";
    }
    public CursoVO(int codigo, String nome, String descricao) {
        this();
        this.codigo = codigo;
        this.nome = nome;
        this.descricao = descricao;
    }

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

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    @Override
    public String toString(){
        return codigo + "," + nome + ", " + descricao ;
    }
}
