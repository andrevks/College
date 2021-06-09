package vo;

public class DisciplinaVO {
    private int codigo;
    private String nome;
    private int semestre;
    private int cargahoraria;
    private int curso;

    public DisciplinaVO() {
        this.codigo = 0;
        this.nome = "";
        this.semestre = 1;
        this.cargahoraria = 20;
        this.curso = 0;
    }

    public DisciplinaVO(int codigo, String nome, int semestre, int cargahoraria, int curso) {
        this.codigo = codigo;
        this.nome = nome;
        this.semestre = semestre;
        this.cargahoraria = cargahoraria;
        this.curso = curso;
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

    public int getSemestre() {
        return semestre;
    }

    public void setSemestre(int semestre) {
        this.semestre = semestre;
    }

    public int getCargahoraria() {
        return cargahoraria;
    }

    public void setCargahoraria(int cargahoraria) {
        this.cargahoraria = cargahoraria;
    }

    public int getCurso() {
        return curso;
    }

    public void setCurso(int curso) {
        this.curso = curso;
    }

    @Override
    public String toString() {
        return this.codigo + "," + this.nome +", com carga horaria " + this.cargahoraria +"\n" +
                ", do semestre " + this.semestre + ", e curso de " + this.curso;
    }
}
