package execucao;

import negocio.AlunoNegocio;
import negocio.CursoNegocio;
import negocio.DisciplinaNegocio;
import negocio.NegocioException;
import vo.AlunoVO;
import vo.CursoVO;
import vo.DisciplinaVO;
import vo.EnumSexo;
import vo.EnumUF;

import java.util.List;
import javax.swing.JOptionPane;

public class Principal {
    private static AlunoNegocio alunoNegocio;
    private static CursoNegocio cursoNegocio;
    private static DisciplinaNegocio disciplinaNegocio;

    public static void main(String [] args){

        try{
            alunoNegocio = new AlunoNegocio();
        }catch (NegocioException ex){
            System.out.println("Camada de negocio e pesistencia não iniciada - " + ex.getMessage());
        }
        try{
            cursoNegocio = new CursoNegocio();
        }catch (NegocioException ex){
            System.out.println("Camada de negocio e pesistencia não iniciada - " + ex.getMessage());
        }
        try{
            disciplinaNegocio = new DisciplinaNegocio();
        }catch (NegocioException ex){
            System.out.println("Camada de negocio e pesistencia não iniciada - " + ex.getMessage());
        }

        if(alunoNegocio != null && cursoNegocio != null && disciplinaNegocio != null) {
            EnumMenu opcao = EnumMenu.Sair;
            do {
                try {
                    opcao = exibirMenu();
                    switch (opcao) {
                        case IncluirAluno:
                            incluirAluno();
                            break;
                        case AlterarAluno:
                            alterarAluno();
                            break;
                        case ExcluirAluno:
                            excluirAluno();
                            break;
                        case PesqMatricula:
                            pesquisarPorMatricula();
                            break;
                        case PesqNome:
                            pesquisarPorNome();
                            break;
                        case ListarAlunos:
                            listarAlunos();
                            break;
                        case IncluirCurso:
                            incluirCurso();
                            break;
                        case AlterarCurso:
                            alterarCurso();
                            break;
                        case ExcluirCurso:
                            excluirCurso();
                            break;
                        case PesqCodCurso:
                            pesquisarPorCodigo();
                            break;
                        case PesqNomeCurso:
                            pesquisarPorNomeCurso();
                            break;
                        case ListarCursos:
                            listarCursos();
                            break;
                        case IncluirDisciplina:
                            incluirDisciplina();
                            break;
                        case AlterarDisciplina:
                            alterarDisciplina();
                            break;
                        case ExcluirDisciplina:
                            excluirDisciplina();
                            break;
                        case PesqCodDisciplina:
                            pesquisarPorCodDisciplina();
                            break;
                        case PesqNomeDisciplina:
                            pesquisarPorNomeDisciplina();
                            break;
                        case ListarDisciplinas:
                            listarDisciplinas();
                    }
                } catch (NegocioException ex) {
                    System.out.println("Operacao nao realizada corretamente - " + ex.getMessage());
                }
            } while (opcao != EnumMenu.Sair);
        }
        System.exit(0);
    }

    //---------------------------DISCIPLINA-------------------------
    /**
     Inclui um nova disciplina na base de dados
     @throws NegocioException
     */
    private static void incluirDisciplina() throws NegocioException {
        DisciplinaVO discTemp = lerDadosDisciplina();
        disciplinaNegocio.inserir(discTemp);
    }

    /**
     * Permite a alteracao dos dados de uma disciplina por meio de codigo
     *
     * @throws NegocioException
     * */
    private static void alterarDisciplina() throws NegocioException {
        int codigo = 0;
        try {
            codigo = Integer.parseInt(JOptionPane.showInputDialog(null,"" +
                    "Forneca o codigo da disciplina", "Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        }catch (Exception ex){
            JOptionPane.showMessageDialog(null, "Digitacao incosistente - " + ex.getMessage());
        }
        DisciplinaVO disciplinaVO = disciplinaNegocio.pesquisaCodigo(codigo);
        if(disciplinaVO != null){
            DisciplinaVO discTemp = lerDadosDisciplina(disciplinaVO);
            disciplinaNegocio.alterar(discTemp);
        } else JOptionPane.showMessageDialog(null, "Curso nao localizado");
    }

    /**
     * Exclui uma disciplina por meio de um codigo fornecida.
     *
     * @throws NegocioException
     * */
    private static void excluirDisciplina() throws NegocioException {
        int codigo = 0;
        try{
            codigo = Integer.parseInt(JOptionPane.showInputDialog(null, "" +
                    "Forneca o codigo da disciplina ","Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        }catch (Exception ex){
            JOptionPane.showMessageDialog(null,"Digitacao inconsistente - " + ex.getMessage());
        }

        DisciplinaVO disciplinaVO = disciplinaNegocio.pesquisaCodigo(codigo);
        if(disciplinaVO != null){
            cursoNegocio.excluir(disciplinaVO.getCodigo());
        } else{
            JOptionPane.showMessageDialog(null, "Disciplina nao localizada");
        }
    }

    /**
     * Pesquisa uma disciplina por meio do codigo.
     *
     * @throws NegocioException
     * */
    private static void pesquisarPorCodDisciplina() throws NegocioException {
        int codigo = 0;
        try {
            codigo = Integer.parseInt(JOptionPane.showInputDialog(null, "" +
                    "Forneca o codigo da disciplina","Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        } catch (Exception ex){
            JOptionPane.showMessageDialog(null, "Digitacao inconsistente - " + ex.getMessage());
        }
        DisciplinaVO disciplinaVO = disciplinaNegocio.pesquisaCodigo(codigo);
        if(disciplinaVO != null){
            mostrarDadosDisciplina(disciplinaVO);
        }else {
            JOptionPane.showMessageDialog(null,"Disciplina nao localizada");
        }
    }

    /**
     * Le um nome ou parte de um nome de uma disciplina e busca no banco de dados
     * disciplinas que possuem esse nome, ou que iniciam com a parte do nome fornecida.
     * Caso nao seja fornecido nenhum valor de entrada sera retornado
     * as 10 primeiras disciplinas ordenados pelo nome.
     * @throws NegocioException
     */
    private static void pesquisarPorNomeDisciplina() throws NegocioException {
        String nome = JOptionPane.showInputDialog(null, "Forneca" +
                "o nome da disciplina", "Leitura de Dados",JOptionPane.QUESTION_MESSAGE);
        if(nome != null){
            List<DisciplinaVO> listaDisciplinaVO = disciplinaNegocio.pesquisaParteNome(nome);

            if(listaDisciplinaVO.size() > 0){
                for(DisciplinaVO disciplinaVO : listaDisciplinaVO) {
                    mostrarDadosDisciplina(disciplinaVO);
                }
            }else{
                JOptionPane.showMessageDialog(null, "Disciplina nao localizada");
            }
        }else{
            JOptionPane.showMessageDialog(null, "Nome nao pode ser nulo");
        }

    }

    /**
     * Busca as disciplina cadastradas.
     *
     */
    private static void listarDisciplinas() throws NegocioException {

        List<DisciplinaVO> listaDisc = disciplinaNegocio.listaDisciplinas();

        if(listaDisc.size() > 0){
            for(DisciplinaVO disciplinaVO : listaDisc) {
                mostrarDadosDisciplinas(disciplinaVO);
            }
        }else{
            JOptionPane.showMessageDialog(null, "Nome nao pode ser nulo");
        }

    }
    /**
     * Exibe no console da aplicacao os dados das disciplinas recebidas pelo parametro disciplinaVO.
     *
     * @param disciplinaVO
     */
    private static void mostrarDadosDisciplina(DisciplinaVO disciplinaVO){
        if(disciplinaVO != null){
            System.out.println("Codigo: " + disciplinaVO.getCodigo());
            System.out.println("Nome: " + disciplinaVO.getNome());
            System.out.println("Semestre: " + disciplinaVO.getSemestre());
            System.out.println("Carga Horaria: " + disciplinaVO.getCargahoraria());
            System.out.println("Curso: " + disciplinaVO.getCurso());
            System.out.println("--------------------------------------------");
        }
    }

    /**
     * Exibe no console da aplicacao os dados de todas disciplinas.
     *
     * @param disciplinaVO
     */
    private static void mostrarDadosDisciplinas(DisciplinaVO disciplinaVO){
        if(disciplinaVO != null){
            System.out.println("Codigo: " + disciplinaVO.getCodigo());
            System.out.println("Nome: " + disciplinaVO.getNome());
            System.out.println("Semestre: " + disciplinaVO.getSemestre());
            System.out.println("Carga Horaria: " + disciplinaVO.getCargahoraria());
            System.out.println("--------------------------------------------");
        }
    }
    /**
     * Le os dados de uma disciplina exibindo os dados atuais recebidos pelo parametro
     * discTemp. Na alteracao permite que os dados atuais das disciplinas sejam visualizados.
     * Na inclusao sao exibidos os dados inicializados na DisciplinaVO.
     *
     * @param discTemp
     * @return
     */
    private static DisciplinaVO lerDadosDisciplina(DisciplinaVO discTemp) {
        String nome;
        int semestre;
        int cargahoraria;
        int curso;
        try{
            nome = JOptionPane.showInputDialog("Forneca o nome da Disciplina", discTemp.getNome().trim());
            discTemp.setNome(nome);

            semestre = Integer.parseInt(JOptionPane.showInputDialog("Forneca o semestre da Disciplina", discTemp.getSemestre()));
            discTemp.setSemestre(semestre);

            cargahoraria = Integer.parseInt(JOptionPane.showInputDialog("Forneca a carga horaria",discTemp.getCargahoraria()));
            discTemp.setCargahoraria(cargahoraria);

            curso = Integer.parseInt(JOptionPane.showInputDialog("Forneca o codigo do curso vinculado a disciplina", discTemp.getCurso()));
            discTemp.setCurso(curso);
        } catch (Exception ex){
            System.out.println("Digitacao incosistente - " + ex.getMessage());
        }
        return discTemp;
    }

    /**
     * Cria uma nova instacia de DisciplinaVO e chama o metodo lerDadosDisciplina(DisciplinaVO disciplinaVO).
     *
     * @return
     */
    private static DisciplinaVO lerDadosDisciplina() {
       DisciplinaVO discTemp = new DisciplinaVO();
        return lerDadosDisciplina(discTemp);
    }
    //--------------------------------------CURSO----------------------------
    /**
     Inclui um novo curso na base de dados
     @throws NegocioException
     */
    private static void incluirCurso() throws NegocioException {
        CursoVO cursoTemp = lerDadosCurso();
        cursoNegocio.inserir(cursoTemp);
    }

    /**
     * Permite a alteracao dos dados de um aluno por meio da matricula
     *
     * @throws NegocioException
     * */
    private static void alterarCurso() throws NegocioException {
        int codigo = 0;
        try {
            codigo = Integer.parseInt(JOptionPane.showInputDialog(null,"" +
                    "Forneca o codigo do curso", "Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        }catch (Exception ex){
            JOptionPane.showMessageDialog(null, "Digitacao incosistente - " + ex.getMessage());
        }
        CursoVO cursoVO = cursoNegocio.pesquisaCodigo(codigo);
        if(cursoVO != null){
            CursoVO cursotemp = lerDadosCurso(cursoVO);
            cursoNegocio.alterar(cursotemp);
        } else JOptionPane.showMessageDialog(null, "Curso nao localizado");
    }

    /**
     * Exclui um curso por meio de um codigo fornecida.
     *
     * @throws NegocioException
     * */
    private static void excluirCurso() throws NegocioException {
        int codigo = 0;
        try{
            codigo = Integer.parseInt(JOptionPane.showInputDialog(null, "" +
                    "Forneca o codigo do Curso","Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        }catch (Exception ex){
            JOptionPane.showMessageDialog(null,"Digitacao inconsistente - " + ex.getMessage());
        }

        CursoVO cursoVO = cursoNegocio.pesquisaCodigo(codigo);
        if(cursoVO != null){
            cursoNegocio.excluir(cursoVO.getCodigo());
        } else{
            JOptionPane.showMessageDialog(null, "Curso nao localizado");
        }
    }

    /**
     * Pesquisa um curso por meio do codigo.
     *
     * @throws NegocioException
     * */
    private static void pesquisarPorCodigo() throws NegocioException {
        int codigo = 0;
        try {
            codigo = Integer.parseInt(JOptionPane.showInputDialog(null, "" +
                    "Forneca o codigo do Curso","Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        } catch (Exception ex){
            JOptionPane.showMessageDialog(null, "Digitacao inconsistente - " + ex.getMessage());
        }
        CursoVO cursoVO = cursoNegocio.pesquisaCodigo(codigo);
        if(cursoVO != null){
            mostrarDadosCurso(cursoVO);
        }else {
            JOptionPane.showMessageDialog(null,"Curso nao localizado");
        }
    }

    /**
     * Le um nome ou parte de um nome de um curso e busca no banco de dados
     * cursos que possuem esse nome, ou que iniciam com a parte do nome fornecida.
     * Caso nao seja fornecido nenhum valor de entrada sera retornado
     * os 10 primeiros cursos ordenados pelo nome.
     *
     * @throws NegocioException
     */
    private static void pesquisarPorNomeCurso() throws NegocioException {
        String nome = JOptionPane.showInputDialog(null, "Forneca" +
                "o nome do Curso", "Leitura de Dados",JOptionPane.QUESTION_MESSAGE);
        if(nome != null){
            List<CursoVO> listaCursoVO = cursoNegocio.pesquisaParteNome(nome);

            if(listaCursoVO.size() > 0){
                for(CursoVO cursoVO : listaCursoVO) {
                    mostrarDadosCurso(cursoVO);
                }
            }else{
                JOptionPane.showMessageDialog(null, "Curso nao localizado");
            }
        }else{
            JOptionPane.showMessageDialog(null, "Nome nao pode ser nulo");
        }

    }

    private static void listarCursos() throws NegocioException {

        List<CursoVO> listaCursoVO = cursoNegocio.listaCursos();

        if(listaCursoVO.size() > 0){
            for(CursoVO cursoVO : listaCursoVO) {
                mostrarDadosCursos(cursoVO);
            }
        }else{
            JOptionPane.showMessageDialog(null, "Nome nao pode ser nulo");
        }

    }
    /**
     * Exibe no console da aplicacao os dados dos alunos recebidos pelo parametro alunoVO.
     *
     * @param cursoVO
     */
    private static void mostrarDadosCurso(CursoVO cursoVO){
        if(cursoVO != null){
            System.out.println("Codigo: " + cursoVO.getCodigo());
            System.out.println("Nome: " + cursoVO.getNome());
            System.out.println("Descricao: " + cursoVO.getDescricao());
            System.out.println("--------------------------------------------");
        }
    }

    /**
     * Exibe no console da aplicacao os dados dos alunos recebidos pelo parametro alunoVO.
     *
     * @param cursoVO
     */
    private static void mostrarDadosCursos(CursoVO cursoVO){
        if(cursoVO != null){
            System.out.println("Codigo: " + cursoVO.getCodigo());
            System.out.println("Nome: " + cursoVO.getNome());
            System.out.println("--------------------------------------------");
        }
    }

    /**
     * Le os dados de um curso exibindo os dados atuais recebidos pelo parametro
     * cursoTemp. Na alteracao permite que os dados atuais dos cursos sejam visualizados.
     * Na inclusao sao exibidos os dados inicializados no CursoVo.
     *
     * @param cursoVO
     * @return
     */
    private static CursoVO lerDadosCurso(CursoVO cursoVO) {
        String nome,descricao;
        try{
            nome = JOptionPane.showInputDialog("Forneca o nome do Curso", cursoVO.getNome().trim());
            cursoVO.setNome(nome);

            descricao = JOptionPane.showInputDialog("Forneca a descricao do Curso",cursoVO.getDescricao().trim());
            cursoVO.setDescricao(descricao);

        } catch (Exception ex){
            System.out.println("Digitacao incosistente - " + ex.getMessage());
        }
        return cursoVO;
    }

    /**
     * Cria uma nova instacia de CursoVO e chama o metodo lerDados(CursoVO cursoVO).
     *
     * @return
     */
    private static CursoVO lerDadosCurso() {
        CursoVO cursoTemp = new CursoVO();
        return lerDadosCurso(cursoTemp);
    }

    //---------------------------ALUNO---------------------------------

    /**
     Inclui um novo aluno na base de dados
     @throws NegocioException
     */
    private static void incluirAluno() throws NegocioException {
        AlunoVO alunoTemp = lerDados();
        alunoNegocio.inserir(alunoTemp);
    }

    /**
    * Permite a alteracao dos dados de um aluno por meio da matricula
    *
    * @throws NegocioException
    * */
    private static void alterarAluno() throws NegocioException {
        int matricula = 0;
        try {
            matricula = Integer.parseInt(JOptionPane.showInputDialog(null,"" +
                    "Forneca a matricula do Aluno", "Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        }catch (Exception ex){
            JOptionPane.showMessageDialog(null, "Digitacao incosistente - " + ex.getMessage());
        }
        AlunoVO alunoVO = alunoNegocio.pesquisaMatricula(matricula);
        if(alunoVO != null){
            AlunoVO alunoTemp = lerDados(alunoVO);
            alunoNegocio.alterar(alunoTemp);
        } else JOptionPane.showMessageDialog(null, "Aluno nao localizado");
    }

    /**
    * Exclui um aluno por meio de uma matricula fornecida.
    *
    * @throws NegocioException
    * */
    private static void excluirAluno() throws NegocioException {
        int matricula = 0;
        try{
            matricula = Integer.parseInt(JOptionPane.showInputDialog(null, "" +
                    "Forneca a matricula do Aluno","Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        }catch (Exception ex){
            JOptionPane.showMessageDialog(null,"Digitacao inconsistente - " + ex.getMessage());
        }

        AlunoVO alunoVO = alunoNegocio.pesquisaMatricula(matricula);
        if(alunoVO != null){
            alunoNegocio.excluir(alunoVO.getMatricula());
        } else{
           JOptionPane.showMessageDialog(null, "Aluno nao localizado");
        }
    }

    /**
    * Pesquisa um aluno por meio da matricula.
    *
    * @throws NegocioException
    * */
    private static void pesquisarPorMatricula() throws NegocioException {
        int matricula = 0;
        try {
            matricula = Integer.parseInt(JOptionPane.showInputDialog(null, "" +
                    "Forneca a matricula do Aluno","Leitura de Dados",JOptionPane.QUESTION_MESSAGE));
        } catch (Exception ex){
            JOptionPane.showMessageDialog(null, "Digitacao inconsistente - " + ex.getMessage());
        }
        AlunoVO alunoVO = alunoNegocio.pesquisaMatricula(matricula);
        if(alunoVO != null){
            mostrarDados(alunoVO);
        }else {
            JOptionPane.showMessageDialog(null,"Aluno nao localizado");
        }
    }

    /**
     * Le um nome ou parte de um nome de um aluno e busca no banco de dados
     * alunos que possuem esse nome, ou que iniciam com a parte do nome fornecida.
     * Caso nao seja fornecido nenhum valor de entrada sera retornado
     * os 10 primeiros alunos ordenados pelo nome.
     *
     * @throws NegocioException
     */
    private static void pesquisarPorNome() throws NegocioException {
        String nome = JOptionPane.showInputDialog(null, "Forneca" +
                "o nome do Aluno", "Leitura de Dados",JOptionPane.QUESTION_MESSAGE);
        if(nome != null){
            List<AlunoVO> listaAlunoVO = alunoNegocio.pesquisaParteNome(nome);

            if(listaAlunoVO.size() > 0){
                for(AlunoVO alunoVO : listaAlunoVO) {
                    mostrarDados(alunoVO);
                }
            }else{
                JOptionPane.showMessageDialog(null, "Aluno nao localizado");
            }
        }else{
            JOptionPane.showMessageDialog(null, "Nome nao pode ser nulo");
        }

    }

    private static void listarAlunos() throws NegocioException {

            List<AlunoVO> listaAlunoVO = alunoNegocio.listaAlunos();

            if(listaAlunoVO.size() > 0){
                for(AlunoVO alunoVO : listaAlunoVO) {
                    mostrarDadosAlunos(alunoVO);
                }
        }else{
            JOptionPane.showMessageDialog(null, "Nome nao pode ser nulo");
        }

    }

    /**
     * Exibe no console da aplicacao os dados dos alunos recebidos pelo parametro alunoVO.
     *
     * @param alunoVO
     */
    private static void mostrarDados(AlunoVO alunoVO){
        if(alunoVO != null){
            System.out.println("Matricula: " + alunoVO.getMatricula());
            System.out.println("Nome: " + alunoVO.getNome());
            System.out.println("Nome da Mae: " + alunoVO.getNomeMae());
            System.out.println("Nome do Pai: " + alunoVO.getNomePai());
            System.out.println("Sexo: " + alunoVO.getSexo().name());
            if(alunoVO.getEndereco() != null){
                System.out.println("Logradouro: " + alunoVO.getEndereco().getLogradouro());
                System.out.println("Numero: " + alunoVO.getEndereco().getNumero());
                System.out.println("Bairro: " + alunoVO.getEndereco().getBairro());
                System.out.println("Cidade: " + alunoVO.getEndereco().getCidade());
                System.out.println("UF: " + alunoVO.getEndereco().getUf());
            }
            System.out.println("Curso: " + alunoVO.getCurso());
            System.out.println("--------------------------------------------");
        }
    }

    /**
     * Exibe no console da aplicacao os dados matricula, nome e sexo dos alunos recebidos pelo parametro
     * alunoVO.
     *
     * @param alunoVO
     */
    private static void mostrarDadosAlunos(AlunoVO alunoVO){
        if(alunoVO != null){
            System.out.println("Matricula: " + alunoVO.getMatricula());
            System.out.println("Nome: " + alunoVO.getNome());
            System.out.println("Sexo: " + alunoVO.getSexo().name());
            System.out.println("--------------------------------------------");
        }
    }

    /**
     * Le os dados de um aluno exibindo os dados atuais recebidos pelo parametro
     * alunoTemp. Na alteracao permite que os dados atuais dos alunos sejam visualizados.
     * Na inclusao sao exibidos os dados inicializados no AlunoVo.
     *
     * @param alunoTemp
     * @return
     */
    private static AlunoVO lerDados(AlunoVO alunoTemp) {
        String nome;
        String nomeMae;
        String nomePai;
        String logradouro;
        String bairro;
        String cidade;
        int numero;
        int curso;
        EnumSexo sexo;
        EnumUF uf;

        try{
            nome = JOptionPane.showInputDialog("Forneca o nome do Aluno", alunoTemp.getNome().trim());
            alunoTemp.setNome(nome);

            nomeMae = JOptionPane.showInputDialog("Forneca o nome da mae do Aluno", alunoTemp.getNomeMae().trim());
            alunoTemp.setNomeMae(nomeMae);

            nomePai = JOptionPane.showInputDialog("Forneca o nome do pai do Aluno",
                    alunoTemp.getNomePai().trim());
            alunoTemp.setNomePai(nomePai);

            sexo = (EnumSexo) JOptionPane.showInputDialog(null, "" +
                    "Escolha uma Opcao", "Leitura de Dados",
                    JOptionPane.QUESTION_MESSAGE, null, EnumSexo.values(), alunoTemp.getSexo());
            alunoTemp.setSexo(sexo);

            logradouro = JOptionPane.showInputDialog("Forneca o logradouro do endereco",
                    alunoTemp.getEndereco().getLogradouro().trim());
            alunoTemp.getEndereco().setLogradouro(logradouro);

            numero = Integer.parseInt(JOptionPane.showInputDialog("Forneca o numero no endereco",
                    alunoTemp.getEndereco().getNumero()));
            alunoTemp.getEndereco().setNumero(numero);

            bairro = JOptionPane.showInputDialog("Forneca o bairro no endereco",
                    alunoTemp.getEndereco().getBairro().trim());
            alunoTemp.getEndereco().setBairro(bairro);

            cidade = JOptionPane.showInputDialog("Forneca a cidade no endereco",alunoTemp.getEndereco().getCidade().trim());
            alunoTemp.getEndereco().setCidade(cidade);

            uf = (EnumUF) JOptionPane.showInputDialog(null, "Escolha uma Opcao",
                    "Leitura de Dados", JOptionPane.QUESTION_MESSAGE, null,EnumUF.values(),
                    alunoTemp.getEndereco()) ;
            alunoTemp.getEndereco().setUf(uf);

            curso = Integer.parseInt(JOptionPane.showInputDialog("Forneca o codigo do curso",alunoTemp.getCurso()));
            alunoTemp.setCurso(curso);
        } catch (Exception ex){
            System.out.println("Digitacao incosistente - " + ex.getMessage());
        }
        return alunoTemp;
    }

    /**
     * Cria uma nova instacia de AlunoVO e chama o metodo lerDados(AlunoVO alunoVO).
     *
     * @return
     */
    private static AlunoVO lerDados() {
        AlunoVO alunoTemp = new AlunoVO();
        return lerDados(alunoTemp);
    }

    /**
     * Exibe as opcoes por meio de uma tela de dialogo.
     *
     * @return
     */
    private static EnumMenu exibirMenu() {
        EnumMenu opcao;

        opcao = (EnumMenu) JOptionPane.showInputDialog(null,
                "Escolha uma Opcao", "Menu",
                JOptionPane.QUESTION_MESSAGE, null, EnumMenu.values(),
                EnumMenu.values()[0]);
        if(opcao == null){
            JOptionPane.showInputDialog(null, "Nenhuma Opcao Escolhida");
            opcao = EnumMenu.Sair;
        }
        return opcao;
    }

}
