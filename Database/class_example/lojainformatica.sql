--DDL - Estrutura
CREATE TABLE estado (
	sigla		char(2)		NOT NULL	UNIQUE,
	descricao	varchar(30),
	CONSTRAINT pkestado PRIMARY KEY(sigla)
);

CREATE TABLE cidade (
	idcidade	SERIAL		NOT NULL,
	nome		VARCHAR(30)	NOT NULL,
	ddd			CHAR(2)		NOT NULL,
	uf			CHAR(2)		NOT NULL,
	CONSTRAINT pkcidade PRIMARY KEY(idcidade),
	CONSTRAINT fkcidade_estado FOREIGN KEY(uf) REFERENCES estado(sigla)
);

CREATE TABLE bairro (
	idbairro	SERIAL		NOT NULL,
	nome		VARCHAR(30)	NOT NULL,
	idcidade	INTEGER		NOT NULL,
	CONSTRAINT pkbairro PRIMARY KEY(idbairro),
	CONSTRAINT fkbairro_cidade FOREIGN KEY(idcidade) REFERENCES cidade(idcidade)
);

CREATE TABLE filial (
	idfilial	SERIAL		NOT NULL,
	rua		VARCHAR(30)	NOT NULL,
	cep		CHAR(9)		NOT NULL,
	numero		CHAR(6)		NOT NULL,
	telefone	CHAR(14)	NOT NULL,
	complemento	VARCHAR(30),
	idbairro	INTEGER		NOT NULL,
	CONSTRAINT pkfilial PRIMARY KEY(idfilial),
	CONSTRAINT fkfilial_bairro FOREIGN KEY(idbairro) REFERENCES bairro(idbairro)
);

CREATE TABLE funcao (
	idfuncao	SERIAL		NOT NULL,
	nome		VARCHAR(30)	NOT NULL 	UNIQUE,
	descricao	VARCHAR(255),
	CONSTRAINT pkfuncao PRIMARY KEY(idfuncao)
);

CREATE TABLE funcionario (
	idfuncionario	SERIAL		NOT NULL,
	nome		VARCHAR(60)	NOT NULL,
	salario		NUMERIC(7,2)	NOT NULL,
	email		VARCHAR(30)	NOT NULL	UNIQUE,
	rua		VARCHAR(30)	NOT NULL,
	cep		CHAR(9)		NOT NULL,
	numero		CHAR(6)		NOT NULL	DEFAULT 'SN',
	telefone	CHAR(14)	NOT NULL,
	complemento	VARCHAR(30),
	idbairro	INTEGER		NOT NULL,
	idfilial	INTEGER		NOT NULL,
	idfuncao	INTEGER		NOT NULL,
	CONSTRAINT pkfuncionario PRIMARY KEY(idfuncionario),
	CONSTRAINT fkfuncionario_bairro FOREIGN KEY(idbairro) REFERENCES bairro(idbairro),
	CONSTRAINT fkfuncionario_filial FOREIGN KEY(idfilial) REFERENCES filial(idfilial),
	CONSTRAINT fkfuncionario_funcao FOREIGN KEY(idfuncao) REFERENCES funcao(idfuncao)
);

CREATE TABLE tipo_produto (
	idtipo_produto	SERIAL		NOT NULL,
	nome			VARCHAR(30)	NOT NULL	UNIQUE,
	descricao		VARCHAR(100),
	CONSTRAINT pktipo_produto PRIMARY KEY (idtipo_produto)
);

CREATE TABLE fornecedor (
	idfornecedor	SERIAL		NOT NULL,
	nome			VARCHAR(50)	NOT NULL,
	cnpj			CHAR(18)	NOT NULL	UNIQUE,
	telefone		CHAR(14) 	NOT NULL,
	email			VARCHAR(30)	NOT NULL,
	CONSTRAINT pkfornecedor PRIMARY KEY (idfornecedor)
);

CREATE TABLE produto (
	idproduto		SERIAL			NOT NULL,
	nome			VARCHAR(100)	NOT NULL,
	descricao		VARCHAR(100)	NOT NULL,
	preco			NUMERIC(7,2)	NOT NULL,
	idfornecedor	INTEGER			NOT NULL,
	idtipo_produto	INTEGER			NOT NULL,
	CONSTRAINT pkproduto PRIMARY KEY (idproduto),
	CONSTRAINT fkproduto_fornecedor FOREIGN KEY(idfornecedor) REFERENCES fornecedor(idfornecedor),
	CONSTRAINT fkproduto_tipoproduto FOREIGN KEY(idtipo_produto) REFERENCES tipo_produto(idtipo_produto)
);

CREATE INDEX idx_produto_nome ON produto USING btree (nome);

CREATE TABLE produto_filial (
	idproduto_filial	SERIAL		NOT NULL,
	idproduto		INTEGER		NOT NULL,
	idfilial		INTEGER		NOT NULL,
	qtde			INTEGER		NOT NULL,
	CONSTRAINT pkproduto_filial PRIMARY KEY(idproduto_filial),
	CONSTRAINT fkprodutofilial_produto FOREIGN KEY(idproduto) REFERENCES produto(idproduto),
	CONSTRAINT fkprodutofilial_filial FOREIGN KEY(idfilial) REFERENCES filial(idfilial)
);

CREATE TABLE tipo_servico (
	idtipo_servico	SERIAL		NOT NULL,
	nome		VARCHAR(30)	NOT NULL	UNIQUE,
	descricao	VARCHAR(255),
	CONSTRAINT pktipo_servico PRIMARY KEY (idtipo_servico)
);

CREATE TABLE servico (
	idservico		SERIAL		NOT NULL,
	nome			VARCHAR(50)	NOT NULL	UNIQUE,
	descricao		VARCHAR(255)	NOT NULL,
	estimativa_tempo	INTEGER,
	preco			NUMERIC(7,2)	NOT NULL,
	idtipo_servico		INTEGER		NOT NULL,
	CONSTRAINT pkservico PRIMARY KEY (idservico),
	CONSTRAINT fkservico_tiposervico FOREIGN KEY(idtipo_servico) REFERENCES tipo_servico(idtipo_servico)
);

CREATE TABLE servico_filial (
	idservico_filial	SERIAL		NOT NULL,
	idservico		INTEGER		NOT NULL,
	idfilial		INTEGER		NOT NULL,
	CONSTRAINT pkservico_filial PRIMARY KEY(idservico_filial),
	CONSTRAINT fkservicofilial_servico FOREIGN KEY(idservico) REFERENCES servico(idservico),
	CONSTRAINT fkservicofilial_filial FOREIGN KEY(idfilial) REFERENCES filial(idfilial)
);

CREATE TABLE cliente (
	idcliente	SERIAL		NOT NULL,
	nome		VARCHAR(60)	NOT NULL,
	email		VARCHAR(30),
	rua		VARCHAR(30)	NOT NULL,
	cep		CHAR(9)		NOT NULL,
	numero		CHAR(6)		NOT NULL,
	telefone	CHAR(14),
	complemento	VARCHAR(30),
	idbairro	INTEGER		NOT NULL,
	CONSTRAINT pkcliente PRIMARY KEY(idcliente),
	CONSTRAINT fkcliente_bairro FOREIGN KEY(idbairro) REFERENCES bairro(idbairro)
);

CREATE INDEX idx_cliente_nome ON cliente(nome);

CREATE TABLE compra (
	idcompra	SERIAL		NOT NULL,
	notafiscal	VARCHAR(30)	NOT NULL,
	data		TIMESTAMP	NOT NULL,
	idcliente	INTEGER		NOT NULL,
	idvendedor	INTEGER		NOT NULL,
	idcaixa		INTEGER		NOT NULL,
	CONSTRAINT pkcompra PRIMARY KEY(idcompra),
	CONSTRAINT fkcompra_funcionariov FOREIGN KEY(idvendedor) REFERENCES funcionario(idfuncionario),
	CONSTRAINT fkcompra_funcionarioc FOREIGN KEY(idcaixa) REFERENCES funcionario(idfuncionario)
);

CREATE TABLE item_compra (
	idcompra		INTEGER		NOT NULL,
	idproduto_filial	INTEGER		NOT NULL,
	valor_unitario		NUMERIC(7,2)	NOT NULL,
	qtde			INTEGER		NOT NULL,
	CONSTRAINT pkitem_compra PRIMARY KEY (idcompra,idproduto_filial),
	CONSTRAINT fkitemcompra_compra FOREIGN KEY (idcompra) REFERENCES compra(idcompra),
	CONSTRAINT fkitemcompra_produtofilial FOREIGN KEY (idproduto_filial) REFERENCES produto_filial(idproduto_filial)
);

CREATE TABLE aquisicao_servico (
	idaquisicao	SERIAL		NOT NULL,
	data		TIMESTAMP	NOT NULL,
	notafiscal	VARCHAR(30)	NOT NULL,
	idcliente	INTEGER		NOT NULL,
	CONSTRAINT pkaquisicao PRIMARY KEY (idaquisicao),
	CONSTRAINT fkaquisicao_cliente FOREIGN KEY (idcliente) REFERENCES cliente(idcliente)
);

CREATE TABLE item_servico (
	iditem_servico		SERIAL		NOT NULL,
	idaquisicao		INTEGER		NOT NULL,
	idservico_filial	INTEGER		NOT NULL,
	valor			NUMERIC(7,2)	NOT NULL,
	CONSTRAINT pkitem_servico PRIMARY KEY (iditem_servico),
	CONSTRAINT fkitemservico_aquisicao FOREIGN KEY (idaquisicao) REFERENCES aquisicao_servico(idaquisicao),
	CONSTRAINT fkitemservico_servicofilial FOREIGN KEY (idservico_filial) REFERENCES servico_filial(idservico_filial)
);


--DML - Dados
INSERT INTO estado (sigla,descricao) VALUES ('MT','Mato Grosso');
INSERT INTO estado (sigla,descricao) VALUES ('MS','Mato Grosso do Sul');

INSERT INTO cidade (nome, ddd, uf) VALUES ('Cuiabá','65','MT');
INSERT INTO cidade (nome, ddd, uf) VALUES ('Campo Grande','67','MS');

INSERT INTO bairro (nome,idcidade) VALUES ('Jd Aclimação', 1);
INSERT INTO bairro (nome,idcidade) VALUES ('Boa Esperança', 1);
INSERT INTO bairro (nome,idcidade) VALUES ('Nova Valentina', 2);
INSERT INTO bairro (nome,idcidade) VALUES ('Distante', 2);

INSERT INTO filial (rua, cep, numero, telefone, idbairro) VALUES ('Rua A','11111-111','1','(11) 1111-1111',1);
INSERT INTO filial (rua, cep, numero, telefone, idbairro) VALUES ('Rua B','22222-222','2','(22) 2222-2222',2);
INSERT INTO filial (rua, cep, numero, telefone, idbairro) VALUES ('Rua C','33333-333','3','(33) 3333-3333',3);
INSERT INTO filial (rua, cep, numero, telefone, idbairro) VALUES ('Rua D','44444-444','4','(44) 4444-4444',4);

INSERT INTO funcao (nome) VALUES ('CAIXA');
INSERT INTO funcao (nome) VALUES ('VENDEDOR');

INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Alberto',1500,'(11) 1234-1234','alberto@gmail.com','Rua X','00000-000',1,1,1);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Alessandra',1000,'(11) 1212-1212','alessandra@live.com','Rua Y','00001-001',1,1,2);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Betina',1500,'(22) 1234-1234','betina@gmail.com','Rua A','10000-000',2,2,1);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Bruno',1000,'(22) 1212-1212','bruno@gmail.com','Rua B','10001-001',2,2,2);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Carlos',1500,'(33) 1234-1234','carlos@gmail.com','Rua C','20000-000',3,3,1);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Carla',1000,'(33) 1212-1212','carla@outlook.com','Rua D','20001-001',3,3,2);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Daniela',1500,'(44) 1234-1234','daniela@gmail.com','Rua F','30000-000',4,4,1);
INSERT INTO funcionario (nome, salario, telefone, email, rua, cep, idbairro, idfilial, idfuncao) VALUES ('Daniel',1000,'(44) 1212-1212','daniel@live.com','Rua G','30001-001',4,4,2);

INSERT INTO fornecedor (nome,cnpj,telefone,email) VALUES ('Samsung','00.000.000/0000-00','(00) 0000-0000','vendas@samsung.com.br');
INSERT INTO fornecedor (nome,cnpj,telefone,email) VALUES ('LG','11.111.111/1111-11','(11) 1111-1111','vendas@lg.com.br');

INSERT INTO tipo_produto(nome) VALUES ('IMPRESSORA');
INSERT INTO tipo_produto(nome) VALUES ('MONITOR');

INSERT INTO produto (nome,descricao,preco,idtipo_produto,idfornecedor) VALUES ('Impressora Samsung S1022','Impressora Jato de Tinta 20ppm',450,1,1);
INSERT INTO produto (nome,descricao,preco,idtipo_produto,idfornecedor) VALUES ('Impressora Samsung S3010','Impressora Laser mono 15ppm',800,1,1);
INSERT INTO produto (nome,descricao,preco,idtipo_produto,idfornecedor) VALUES ('Impressora LG','Impressora Jato de Tinta 18ppm',520,1,2);
INSERT INTO produto (nome,descricao,preco,idtipo_produto,idfornecedor) VALUES ('Monitor LG 24','Monitor 24 Full HD 60hz',1400,2,2);

INSERT INTO produto_filial (idproduto,idfilial,qtde) VALUES (1,1,3);
INSERT INTO produto_filial (idproduto,idfilial,qtde) VALUES (1,3,2);
INSERT INTO produto_filial (idproduto,idfilial,qtde) VALUES (2,1,2);
INSERT INTO produto_filial (idproduto,idfilial,qtde) VALUES (2,4,4);
INSERT INTO produto_filial (idproduto,idfilial,qtde) VALUES (3,2,1);

INSERT INTO tipo_servico (nome) VALUES ('LIMPEZA');
INSERT INTO tipo_servico (nome) VALUES ('MONTAGEM');

INSERT INTO servico (nome,descricao,preco,idtipo_servico) VALUES ('Limpeza de CPU','Limpeza de CPU',50,1);
INSERT INTO servico (nome,descricao,preco,idtipo_servico) VALUES ('Limpeza de Impressora','Limpeza de Impressora',40,1);
INSERT INTO servico (nome,descricao,preco,idtipo_servico) VALUES ('Montagem de PC','Montagem de PC Simples',200,2);
INSERT INTO servico (nome,descricao,preco,idtipo_servico) VALUES ('Montagem de PC Gamer','Montagem de PC Gamer',350,2);

INSERT INTO servico_filial (idservico,idfilial) VALUES (1,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (1,2);
INSERT INTO servico_filial (idservico,idfilial) VALUES (1,3);
INSERT INTO servico_filial (idservico,idfilial) VALUES (1,4);
INSERT INTO servico_filial (idservico,idfilial) VALUES (2,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (2,2);
INSERT INTO servico_filial (idservico,idfilial) VALUES (2,3);
INSERT INTO servico_filial (idservico,idfilial) VALUES (2,4);
INSERT INTO servico_filial (idservico,idfilial) VALUES (3,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (3,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (3,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (3,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (4,1);
INSERT INTO servico_filial (idservico,idfilial) VALUES (4,2);

INSERT INTO cliente (nome,email,rua,cep,numero,idbairro) VALUES ('Adriana','adriana@gmail.com','Rua A','00000-000','0',1);
INSERT INTO cliente (nome,email,rua,cep,numero,idbairro) VALUES ('Bruno','bruno@gmail.com','Rua B','11111-000','1',2);
INSERT INTO cliente (nome,email,rua,cep,numero,idbairro) VALUES ('Carlos','carlos@outlook.com','Rua C','22222-000','2',3);
INSERT INTO cliente (nome,email,rua,cep,numero,idbairro) VALUES ('Daniela','daniela@yahoo.com','Rua D','33333-000','3',4);
INSERT INTO cliente (nome,email,rua,cep,numero,idbairro) VALUES ('Everaldo','everaldo@outlook.com','Rua E','44444-000','4',1);
INSERT INTO cliente (nome,email,rua,cep,numero,idbairro) VALUES ('Flávia','flavia@ifmt.edu.br','Rua F','55555-000','5',2);

INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('1',date '2021-01-01',1,2,1);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('2',date '2021-01-10',3,4,3);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('3',date '2021-01-15',1,6,5);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('4',date '2021-01-25',2,2,1);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('5',date '2021-03-02',4,2,1);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('6',date '2021-03-08',5,8,7);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('7',date '2021-03-17',2,8,7);
INSERT INTO compra (notafiscal,data,idcliente,idvendedor,idcaixa) VALUES ('8',date '2021-03-21',6,4,3);

INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (1,1,450,1);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (1,3,800,1);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (2,5,520,1);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (3,2,450,2);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (4,3,800,1);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (5,1,450,3);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (6,4,800,1);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (7,4,800,1);
INSERT INTO item_compra (idcompra,idproduto_filial,valor_unitario,qtde) VALUES (8,5,520,1);

INSERT INTO aquisicao_servico (data,notafiscal,idcliente) VALUES (,'',);

INSERT INTO item_servico (idaquisicao,idservico_filial,valor) VALUES (,,);



--DQL (Data Query Language)
SELECT c.*, e.descricao
FROM cidade c, estado e
WHERE c.uf = e.sigla

SELECT c.*, e.descricao as estado
FROM cidade c INNER JOIN estado e ON c.uf = e.sigla

SELECT b.nome as bairro, c.nome as cidade, c.uf, e.descricao as estado
FROM bairro b, cidade c, estado e
WHERE b.idcidade = c.idcidade AND 
      c.uf = e.sigla;

SELECT b.nome as bairro, c.nome as cidade, c.uf, e.descricao as estado
FROM bairro b INNER JOIN cidade c ON b.idcidade = c.idcidade
              INNER JOIN estado e ON c.uf = e.sigla;

SELECT f.*, b.nome as bairro, c.nome as cidade, c.uf, e.descricao as estado
FROM bairro b INNER JOIN cidade c ON b.idcidade = c.idcidade
              INNER JOIN estado e ON c.uf = e.sigla
  	      INNER JOIN filial f ON f.idbairro = b.idbairro

--EXPLORAR EM FUNÇÕES AUXILIARES PARA DATE/TIME E STRING.

SELECT idfilial, COUNT(idfilial) as qtdefuncionario, AVG(salario), MAX(salario),MIN(salario)
FROM funcionario fu INNER JOIN filial fi ON fu.idfilial = fi.idfilial
GROUP BY fi.nome

--Menos performático 69ms (32% mais lento)
SELECT ci.nome, COUNT(ci.nome) as qtdecompra
FROM compra co INNER JOIN cliente ci ON co.idcliente = ci.idcliente
WHERE ci.nome = 'Adriana'
GROUP BY ci.nome

--Mais performático 52ms
SELECT c.nome, compras.qtdecompra
FROM cliente c INNER JOIN
	(SELECT co.idcliente, COUNT(idcliente) as qtdecompra
	FROM compra co
	GROUP BY co.idcliente
	HAVING idcliente = 1) compras ON c.idcliente = compras.idcliente 

SELECT 
FROM bairro b INNER JOIN cidade c ON b.idcidade = c.idcidade
              INNER JOIN estado e ON c.uf = e.sigla

SELECT c.nome, bairros.qtde
FROM cidade c INNER JOIN 
	(SELECT idcidade, COUNT(idcidade)as qtde
	FROM bairro
	GROUP BY (idcidade)) bairros ON c.idcidade = bairros.idcidade

SELECT c.uf, COUNT(c.uf) as qtdebairros
FROM bairro b INNER JOIN cidade c ON b.idcidade = c.idcidade
GROUP BY c.uf







--RELATORIOS

--Quais filiais possuem determinado produto disponível em estoque? 
SELECT f.rua as filial, pf.qtde
FROM
	(SELECT *
	FROM produto_filial
	WHERE idproduto = (SELECT idproduto FROM produto WHERE LOWER(nome) LIKE '%impressora%s3010%')
	                   AND qtde > 0) pf INNER JOIN filial f ON pf.idfilial = f.idfilial;

--Relação dos produtos mais vendidos. 
SELECT produto.nome, vendas.qtdetotal
FROM 
	(SELECT pf.idproduto, SUM(ic.qtde) as qtdetotal
	FROM item_compra ic INNER JOIN produto_filial pf ON ic.idproduto_filial = pf.idproduto_filial
	GROUP BY pf.idproduto) vendas INNER JOIN produto ON vendas.idproduto = produto.idproduto
ORDER BY vendas.qtdetotal DESC;

--Relação dos serviços mais vendidos. Idem ao anterior

--Qual o faturamento anual por filial?
SELECT TO_CHAR(c.data,'yyyy') as ano, pf.idfilial, SUM(ic.qtde*ic.valor_unitario) as total
FROM item_compra ic INNER JOIN produto_filial pf ON ic.idproduto_filial = pf.idproduto_filial
     INNER JOIN compra c ON c.idcompra = ic.idcompra
GROUP BY TO_CHAR(c.data,'yyyy'), pf.idfilial
ORDER BY TO_CHAR(c.data,'yyyy') ASC, SUM(ic.qtde*ic.valor_unitario) DESC;

--Qual o capital (R$) em estoque na empresa?
SELECT SUM (p.preco*pf.qtde) as total
FROM produto p INNER JOIN produto_filial pf ON p.idproduto = pf.idproduto; 

--Qual o faturamento de um determinado mês separados por funcionário? 
SELECT f.nome, vendas.totalmes
FROM 
	(SELECT c.idvendedor, SUM(ic.qtde*ic.valor_unitario) as totalmes
	FROM compra c INNER JOIN item_compra ic ON c.idcompra = ic.idcompra
	WHERE TO_CHAR(c.data,'mm/yyyy') = '03/2021'
	GROUP BY c.idvendedor) vendas INNER JOIN funcionario f ON f.idfuncionario = vendas.idvendedor
ORDER BY vendas.totalmes DESC;

--Relação de clientes em ordem decrescente por gasto total de compras? 
SELECT c.nome, c.email, vendas.total
FROM
	(SELECT c.idcliente, SUM(ic.qtde*ic.valor_unitario) as total
	FROM compra c INNER JOIN item_compra ic ON c.idcompra = ic.idcompra
	GROUP BY c.idcliente) as vendas INNER JOIN cliente c ON c.idcliente = vendas.idcliente
ORDER BY vendas.total DESC;

--Quais as compras realizadas por um determinado cliente em ordem decrescente data? 
SELECT co.data, p.nome, ic.qtde, ic.valor_unitario, ic.qtde*ic.valor_unitario as total
FROM cliente c INNER JOIN compra co ON c.idcliente = co.idcliente
               INNER JOIN item_compra ic ON co.idcompra = ic.idcompra
			   INNER JOIN produto_filial pf ON pf.idproduto_filial = ic.idproduto_filial
			   INNER JOIN produto p ON p.idproduto = pf.idproduto
WHERE UPPER(c.nome) LIKE '%ANA%'
ORDER by co.data DESC;

--Relação de faturamento por tipo de produto para um determinado período. 
SELECT tp.nome, vendas.total
FROM tipo_produto tp INNER JOIN
	(SELECT p.idtipo_produto, SUM(ic.qtde*ic.valor_unitario) as total
	FROM compra c INNER JOIN item_compra ic ON c.idcompra = ic.idcompra
				  INNER JOIN produto_filial pf ON ic.idproduto_filial = pf.idproduto_filial
				  INNER JOIN produto p ON p.idproduto = pf.idproduto
	WHERE c.data BETWEEN date '2021-01-15' AND date '2021-04-10'
	GROUP BY p.idtipo_produto) vendas ON tp.idtipo_produto = vendas.idtipo_produto; 

--Relação de faturamento por tipo de serviço para um determinado período. Idem ao anterior.

--Qual o Faturamento médio mensal de cada funcionário? 
SELECT x.idvendedor, AVG(x.total) as media
FROM
	(SELECT TO_CHAR(c.data,'mm/yyyy') as mes, c.idvendedor, SUM(ic.valor_unitario * ic.qtde) as total
	FROM compra c INNER JOIN item_compra ic ON c.idcompra = ic.idcompra
	GROUP BY TO_CHAR(c.data,'mm/yyyy'), c.idvendedor) x
GROUP BY x.idvendedor;