package negocio;

import persistencia.DisciplinaDAO;
import persistencia.ConexaoBD;
import persistencia.PersistenciaException;
import vo.DisciplinaVO;

import java.util.List;

public class DisciplinaNegocio {
    private DisciplinaDAO disciplinaDAO;

    public DisciplinaNegocio() throws NegocioException {
        try {
            this.disciplinaDAO = new DisciplinaDAO(ConexaoBD.getInstancia());
        }catch (PersistenciaException ex ){
            throw new NegocioException("Erro ao iniciar a Persistencia - " + ex.getMessage());
        }
    }

    public void inserir(DisciplinaVO disciplinaVO) throws NegocioException {
        String mensagemErros = this.validarDados(disciplinaVO);
        if(!mensagemErros.isEmpty()){
            throw new NegocioException(mensagemErros);
        }
        try {
            if(disciplinaDAO.incluir(disciplinaVO) == 0 ){
                throw new NegocioException("Inclusao nao realizada !!");
            }
        }catch (PersistenciaException ex){
            throw new NegocioException("AlunoNegocio: Erro ao incluir a disciplina - " + ex.getMessage());
        }
    }

    public void alterar(DisciplinaVO disciplinaVO) throws NegocioException {
        String mensagemErros = this.validarDados(disciplinaVO);
        if(!mensagemErros.isEmpty()){
            throw new NegocioException(mensagemErros);
        }
        try {
            if(disciplinaDAO.alterar(disciplinaVO) == 0 ){
                throw new NegocioException("Alteracao nao realizada !!");
            }
        }catch (PersistenciaException ex){
            throw new NegocioException("Erro ao alterar a disciplina - " + ex.getMessage());
        }
    }

    public void excluir(int codigo) throws NegocioException {
        try {
            if(disciplinaDAO.excluir(codigo) == 0 ){
                throw new NegocioException("Exclusao nao realizada !!");
            }
        }catch (PersistenciaException ex){
            throw new NegocioException("Erro ao excluir a disciplina - " + ex.getMessage());
        }
    }

    public List<DisciplinaVO> pesquisaParteNome(String parteNome) throws NegocioException {
        try{
            return disciplinaDAO.buscarPorNome(parteNome);
        }catch (PersistenciaException ex) {
            throw new NegocioException("Erro ao pesquisar a disciplina - " + ex.getMessage());
        }
    }

    public DisciplinaVO pesquisaCodigo(int codigo) throws NegocioException {
        try{
            return disciplinaDAO.buscarPorCodigo(codigo);
        }catch (PersistenciaException ex) {
            throw new NegocioException("Erro ao pesquisar a disciplina - " + ex.getMessage());
        }
    }

    private String validarDados(DisciplinaVO disciplinaVO) {
        String mensagemErros = "";
        if(disciplinaVO.getNome() == null || disciplinaVO.getNome().length() == 0){
            mensagemErros += "Nome da disciplina nao pode ser vazio";
        }
        if(disciplinaVO.getSemestre() <= 0){
            mensagemErros += "\n O numero do semestre deve ser maior que ZERO";
        }
        if(disciplinaVO.getCargahoraria() <= 20){
            mensagemErros += "\n A carga horaria deve ser maior que 20";
        }
        if(disciplinaVO.getCurso() <= 0){
            mensagemErros += "\n o codigo do curso deve ser maior que ZERO";
        }

        return mensagemErros;
    }

    public List<DisciplinaVO> listaDisciplinas() throws NegocioException{

        try {
            return disciplinaDAO.listarDisciplinas();
        } catch (PersistenciaException ex) {
            throw new NegocioException("Erro ao listar disciplinas - " + ex.getMessage());
        }

}
}
