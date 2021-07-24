CREATE TABLE moeda (
  codmoeda CHAR(3) NOT NULL,
  nome VARCHAR(25) NOT NULL UNIQUE,
  simbolo VARCHAR(200),
  CONSTRAINT pkmoeda PRIMARY KEY (codmoeda)
);

CREATE TABLE usuario (
  idusuario SERIAL NOT NULL,
  nome VARCHAR(40) NOT NULL, --INDEX
  email VARCHAR(30) NOT NULL UNIQUE,
  senha VARCHAR(12) NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  fone CHAR(10) NOT NULL,
  CONSTRAINT pkusuario PRIMARY KEY (idusuario)
);

CREATE TABLE ordem (
  idordem SERIAL NOT NULL,
  opcao CHAR(10) NOT NULL,
  estado CHAR(10) NOT NULL, --CREATE A INDEX FOR ESTADO
  data DATE NOT NULL,
  quantidade INTEGER NOT NULL,
  valorunitario NUMERIC(10,9) NOT NULL,
  idusuario INTEGER NOT NULL,
  codmoeda CHAR(3) NOT NULL,
  CONSTRAINT pkordem PRIMARY KEY (idordem),
  CONSTRAINT fkordem_usuario FOREIGN KEY(idusuario) REFERENCES usuario(idusuario),
  CONSTRAINT fkordem_moeda FOREIGN KEY(codmoeda) REFERENCES moeda(codmoeda)
);

CREATE TABLE transacao (
  idtransacao SERIAL NOT NULL, 
  tipo_transacao CHAR(10) NOT NULL, --INDEX FOR tipo_transacao
  descricao VARCHAR(30),
  data DATE NOT NULL,
  valor NUMERIC NOT NULL,
  taxa NUMERIC(3,0) NOT NULL,
  idordem INTEGER, --NULL
  CONSTRAINT pktransacao PRIMARY KEY (idtransacao),
  CONSTRAINT fktransacao_ordem FOREIGN KEY(idordem) REFERENCES ordem(idordem)
);

CREATE TABLE banco (
  conta CHAR(10) NOT NULL,
  agencia CHAR(4) NOT NULL,
  CONSTRAINT pkconta PRIMARY KEY (conta)
);

CREATE TABLE deposito (
  iddeposito SERIAL NOT NULL,
  endereco VARCHAR(30) NOT NULL,
  valor NUMERIC NOT NULL,
  idtransacao INTEGER NOT NULL,
  bancoconta CHAR(10) NOT NULL,
  idusuario INTEGER NOT NULL,
  CONSTRAINT pkdeposito PRIMARY KEY (iddeposito),
  CONSTRAINT fkdeposito_transacao FOREIGN KEY (idtransacao) REFERENCES transacao(idtransacao),
  CONSTRAINT fkdeposito_bancoconta FOREIGN KEY (bancoconta) REFERENCES banco(conta),
  CONSTRAINT fkdeposito_usuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE saque (
  idsaque SERIAL NOT NULL,
  endereco VARCHAR(30) NOT NULL,
  valor NUMERIC NOT NULL,
  idtransacao INTEGER NOT NULL,
  idusuario INTEGER NOT NULL,
  CONSTRAINT pksaque PRIMARY KEY (idsaque),
  CONSTRAINT fksaque_transacao FOREIGN KEY (idtransacao) REFERENCES transacao(idtransacao),
  CONSTRAINT fksaque_usuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE carteira (
  idcarteira SERIAL NOT NULL,
  valortotal NUMERIC NOT NULL,
  idusuario INTEGER NOT NULL,
  CONSTRAINT pkcarteira PRIMARY KEY (idcarteira),
  CONSTRAINT fkcarteira_usuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

-- CREATE TABLE carteira_transacao (
--   idcarteira_transacao SERIAL NOT NULL,
--   valor NUMERIC NOT NULL,
--   idtransacao INTEGER NOT NULL,
--   idcarteira INTEGER NOT NULL,
--   CONSTRAINT pkcarteira_transacao PRIMARY KEY (idcarteira_transacao),
--   CONSTRAINT fkcarteira_transacao_transacao FOREIGN KEY (idtransacao) REFERENCES transacao(idtransacao),
--   CONSTRAINT fkcarteira_transacao_carteira FOREIGN KEY (idcarteira) REFERENCES carteira(idcarteira)
-- );

-- INSERT INFO

--MOEDA
INSERT INTO moeda (codmoeda, nome) VALUES ('BTC','Bitcoin');
INSERT INTO moeda (codmoeda, nome) VALUES ('ETH','Ethereum');
INSERT INTO moeda (codmoeda, nome) VALUES ('ADA','Cardano');

SELECT * FROM moeda;
--USUARIO

INSERT INTO usuario(nome, email, senha, cpf, fone) 
VALUES ('Aurora','aurora@banco.com','7509d123bce','21542833140', '6599981234');
INSERT INTO usuario(nome, email, senha, cpf, fone) 
VALUES ('Maria Eduarda','maria@sha.com@banco.com','1aa92331861','22852340747','6589092343');
INSERT INTO usuario(nome, email, senha, cpf, fone)
VALUES ('Joao','joao@conseno.com','cf8fd738a5','86288106259','6589098888');
INSERT INTO usuario(nome, email, senha, cpf, fone)
VALUES ('Lucas','lucas@ordem.com','38a8fd','15633650220','5872365813');

SELECT * FROM usuario;
--ORDEM

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('venda', 'concluido', DATE '2021-06-22',80,1,1,'BTC');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('compra', 'espera', DATE '2021-06-20',240,1,3,'ETH');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('venda', 'concluido', DATE '2021-06-23',200,1,2,'ADA');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('compra', 'concluido', DATE '2021-07-20',755,5,4,'BTC');

SELECT * FROM ordem;

-- TRANSACAO


INSERT INTO transacao(tipo_transacao,descricao, data, valor, taxa, idordem)
VALUES('ordem', 'debito', DATE '2021-06-22',80, 10, 1);

INSERT INTO transacao(tipo_transacao, data, valor, taxa, idordem)
VALUES('ordem', DATE '2021-06-24',200, 10, 3);

INSERT INTO transacao(tipo_transacao, data, valor, taxa)
VALUES('saque', DATE '2021-06-25',50, 10);

INSERT INTO transacao(tipo_transacao, data, valor, taxa)
VALUES('deposito', DATE '2021-06-25',500, 10);


INSERT INTO transacao(tipo_transacao,descricao, data, valor, taxa, idordem)
VALUES('ordem', 'debito', DATE '2021-07-20',755, 10, 4);

INSERT INTO transacao(tipo_transacao, data, valor, taxa)
VALUES('saque', DATE '2021-07-20',100, 10);

INSERT INTO transacao(tipo_transacao, data, valor, taxa)
VALUES('deposito', DATE '2021-07-20', 4000, 10);

INSERT INTO transacao(tipo_transacao, data, valor, taxa)
VALUES('saque', DATE '2021-07-21',200, 10);

INSERT INTO transacao(tipo_transacao, data, valor, taxa)
VALUES('deposito', DATE '2021-07-21', 337, 10);

SELECT * FROM transacao;

SELECT * FROM usuario;

SELECT * FROM ordem;

-- SAQUE

INSERT INTO saque(endereco, valor,idtransacao,idusuario)
VALUES('5170e7e806',50, 3, 1);

INSERT INTO saque(endereco, valor,idtransacao,idusuario)
VALUES('a9a8066170',100, 6, 2);

INSERT INTO saque(endereco, valor,idtransacao,idusuario)
VALUES('aww3231230',200, 8, 3);

SELECT * FROM saque;

-- BANCO 

INSERT INTO banco(conta, agencia)
VALUES('1093135-X','2624');

INSERT INTO banco(conta, agencia)
VALUES('1191984-1','3628');

INSERT INTO banco(conta, agencia)
VALUES('23635-0','0097');

SELECT * FROM banco;

-- DEPOSITO


INSERT INTO deposito(endereco, valor, idtransacao,bancoconta,idusuario)
VALUES('5170e7e806', 500, 4, '1093135-X', 1);

INSERT INTO deposito(endereco, valor, idtransacao,bancoconta, idusuario)
VALUES('21321aa708', 4000, 7, '1191984-1', 3);

INSERT INTO deposito(endereco, valor, idtransacao,bancoconta, idusuario)
VALUES('213yyy983', 337, 9, '23635-0', 4);

SELECT * FROM deposito;


-- CARTEIRA

INSERT INTO carteira(valortotal, idusuario)
VALUES(1000, 1);

INSERT INTO carteira(valortotal, idusuario)
VALUES(1200, 2);

INSERT INTO carteira(valortotal, idusuario)
VALUES(750, 3);

INSERT INTO carteira(valortotal, idusuario)
VALUES(1500, 4);

SELECT * FROM carteira;

-- -- CARTEIRA-TRANSACAO

-- INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
-- VALUES(80, 1, 1);

-- INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
-- VALUES(200, 2, 2);

-- INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
-- VALUES(50, 3, 3);

-- INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
-- VALUES(500, 4, 3);
-- SELECT * FROM carteira_transacao;

SELECT * FROM banco;
SELECT * FROM carteira;
SELECT * FROM deposito;
SELECT * FROM moeda;
SELECT * FROM ordem;
SELECT * FROM saque;
SELECT * FROM transacao;
SELECT * FROM usuario;

--INDEX

CREATE INDEX idx_usuario_nome ON usuario USING btree(nome);

CREATE INDEX idx_ordem_estado ON ordem USING hash(estado);

CREATE INDEX idx_transacao_tipo_transacao ON transacao USING hash(tipo_transacao);


--RELATORIOS

-- Quais clientes fizeram transações de compra e venda em um determinado dia ? e quais os valores negociados ?

SELECT u.nome, o.opcao as tipo, t.valor
FROM ordem o INNER JOIN transacao t ON o.idordem = t.idordem
		     INNER JOIN usuario u ON u.idusuario = o.idusuario
WHERE t.data = '2021-07-20';


-- Quais as moedas com maior market cap ? 
--market cap: It’s calculated by multiplying the number of coins in circulation by the current market price of a single coin.

SELECT o.codmoeda as moeda, SUM(t.valor) as market_cap
FROM transacao t INNER JOIN ordem o ON o.idordem = t.idordem
GROUP BY o.codmoeda
ORDER BY SUM(t.valor) DESC;
 


-- A nossa rentabilidade vem através das taxas das transações, sabendo disso, qual a rentabilidade mensal ?
--(neste caso, inclui todos os tipos de transação, ordem, deposito e saque)
  
  SELECT TO_CHAR(t.data,'mm-yyyy') mes_ano, SUM(t.valor * (t.taxa/100)) as valor_mensal
  FROM transacao t 
  GROUP BY TO_CHAR(t.data,'mm-yyyy');
 
 
-- Qual a média da quantidade de transações do tipo ordem feitas mensalmente?
-- REFORMULANDO: Qual a quantidade e valor médio das transações do tipo ordem feitas mensalmente?
  
  SELECT TO_CHAR(t.data,'mm-yyyy') mes_ano, COUNT(t.idtransacao) as qtd, AVG(t.valor) valor_medio
  FROM transacao t 
  GROUP BY t.tipo_transacao, TO_CHAR(t.data,'mm-yyyy')
  HAVING t.tipo_transacao = 'ordem';
 
  
-- Quais as moedas mais negociadas e valortotal negociado ?

SELECT o.codmoeda as moeda, COUNT(o.codmoeda) as vezes_negociada, SUM(t.valor) as total_negociado
FROM ordem o INNER JOIN transacao t ON o.idordem = t.idordem 
GROUP BY o.codmoeda;

-- Quais as transações de moedas realizadas por um determinado cliente em ordem do mais recente ao mais antigo ?

SELECT t.data, o.codmoeda as moeda, t.valor, t.taxa
FROM ordem o INNER JOIN transacao t ON o.idordem = t.idordem
WHERE o.idusuario = (SELECT u.idusuario FROM usuario u WHERE LOWER(u.nome) LIKE '%auro%')	
ORDER BY t.data DESC;

-- Qual o faturamento anual por moeda ? 

  SELECT o.codmoeda as moeda , SUM(t.valor * (t.taxa/100)) as valor 
  FROM transacao t INNER JOIN ordem o ON o.idordem = t.idordem
  WHERE TO_CHAR(t.data,'yyyy') = '2021'
  GROUP BY o.codmoeda
  ORDER BY SUM(t.valor * (t.taxa/100)) DESC;
  

-- Qual o faturamento de um determinado mês por moeda ?

  SELECT o.codmoeda as moeda , SUM(t.valor * (t.taxa/100)) as valor 
  FROM transacao t INNER JOIN ordem o ON o.idordem = t.idordem
  WHERE TO_CHAR(t.data,'mm/yyyy') = '06/2021'
  GROUP BY o.codmoeda
  ORDER BY SUM(t.valor * (t.taxa/100)) DESC;
  
-- Relação das moedas mais vendidas/compradas. idem ao "moedas mais negociadas"

-- Qual o histórico dos depósitos/saques de determinado cliente ? 

SELECT d.endereco as end_deposito, d.valor as valor_deposito, d.bancoconta as conta_origem_deposito, 
s.endereco as end_saque, s.valor
FROM deposito d, saque s
		WHERE d.idusuario = (SELECT u.idusuario FROM usuario u WHERE LOWER(u.nome) LIKE '%jo%')	
		AND s.idusuario = d.idusuario;


-- Quais as moedas mais utilizadas como troca em um determinado período ?
-- (inrelevante, já que o sistema mudou de funcionamento, a moeda de troca é sempre o real)


-- Quais moedas sofreram a maior diferença de preço nos últimos 7 dias ?
-- (teria que ter o histórico diário da moeda, com o percentual da variação para conseguir ter precisao nesta informação, 
-- aumentando a complexidade do sistema
