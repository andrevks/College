CREATE TABLE moeda (
  codmoeda SERIAL NOT NULL,
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
  codmoeda INTEGER NOT NULL,
  CONSTRAINT pkordem PRIMARY KEY (idordem),
  CONSTRAINT fkordem_usuario FOREIGN KEY(idusuario) REFERENCES usuario(idusuario),
  CONSTRAINT fkordem_moeda FOREIGN KEY(codmoeda) REFERENCES moeda(codmoeda)
);

CREATE TABLE trasacao (
  idtransacao SERIAL NOT NULL, 
  tipo_trasacao CHAR(10) NOT NULL, --INDEX FOR tipo_transacao
  descricao VARCHAR(250),
  data DATE NOT NULL,
  valor NUMERIC NOT NULL,
  taxa NUMERIC(3,0) NOT NULL,
  idordem INTEGER NOT NULL,
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
  CONSTRAINT pkdeposito PRIMARY KEY (iddeposito),
  CONSTRAINT fkdeposito_transacao FOREIGN KEY (idtransacao) REFERENCES trasacao(idtransacao),
  CONSTRAINT fkdeposito_bancoconta FOREIGN KEY (bancoconta) REFERENCES banco(conta)
);

CREATE TABLE saque (
  idsaque SERIAL NOT NULL,
  endereco VARCHAR(30) NOT NULL,
  valor NUMERIC NOT NULL,
  idtransacao INTEGER NOT NULL,
  idusuario INTEGER NOT NULL,
  CONSTRAINT pksaque PRIMARY KEY (idsaque),
  CONSTRAINT fksaque_transacao FOREIGN KEY (idtransacao) REFERENCES trasacao(idtransacao),
  CONSTRAINT fksaque_usuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE carteira (
  idcarteira SERIAL NOT NULL,
  valortotal NUMERIC NOT NULL,
  idusuario INTEGER NOT NULL,
  CONSTRAINT pkcarteira PRIMARY KEY (idcarteira),
  CONSTRAINT fkcarteira_usuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE carteira_transacao (
  idcarteira_transacao SERIAL NOT NULL,
  valor NUMERIC NOT NULL,
  idtransacao INTEGER NOT NULL,
  idcarteira INTEGER NOT NULL,
  CONSTRAINT pkcarteira_transacao PRIMARY KEY (idcarteira_transacao),
  CONSTRAINT fkcarteira_transacao_transacao FOREIGN KEY (idtransacao) REFERENCES trasacao(idtransacao),
  CONSTRAINT fkcarteira_transacao_carteira FOREIGN KEY (idcarteira) REFERENCES carteira(idcarteira)
);

INSERT INTO moeda (codmoeda, nome) VALUES ('BTC','Bitcoin');
INSERT INTO moeda (codmoeda, nome) VALUES ('ETH','Ethereum');
INSERT INTO moeda (codmoeda, nome) VALUES ('ADA','Cardano');

INSERT INTO usuario(nome, email, senha, cpf, fone) 
VALUES ('Aurora','aurora@banco.com','7509d123bce','21542833140', '6599981234');
INSERT INTO usuario(nome, email, senha, cpf, fone) 
VALUES ('Maria Eduarda','maria@sha.com@banco.com','1aa92331861','22852340747','6589092343');
INSERT INTO usuario(nome, email, senha, cpf, fone)
VALUES ('Joao','joao@conseno.com','cf8fd738a5','86288106259','6589098888');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('credito', 'concluido', DATE '2021-06-22',80,1,2,'BTC');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('debito', 'espera', DATE '2021-06-20',240,1,3,'ETH');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('credito', 'espera', DATE '2021-06-18',50,1,3,'ADA');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('credito', 'concluido', DATE '2021-06-23',200,1,2,'ADA');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('debito', 'concluido', DATE '2021-06-25',50,1,5,'ADA');

INSERT INTO ordem(opcao, estado, data, quantidade, valorunitario, idusuario, codmoeda)
VALUES('credito', 'concluido', DATE '2021-06-25',500,1,5,'BTC');
-- TRANSACAO


INSERT INTO trasacao(tipo_trasacao,descricao, data, valor, taxa, idordem)
VALUES('ordem', 'debito', DATE '2021-06-22',80, 10, 2);

INSERT INTO trasacao(tipo_trasacao, data, valor, taxa, idordem)
VALUES('ordem', DATE '2021-06-24',200, 10, 7);

INSERT INTO trasacao(tipo_trasacao, data, valor, taxa, idordem)
VALUES('saque', DATE '2021-06-25',50, 10, 8);

INSERT INTO trasacao(tipo_trasacao, data, valor, taxa, idordem)
VALUES('deposito', DATE '2021-06-25',500, 10, 9);

-- SAQUE

INSERT INTO saque(endereco, valor,idtransacao,idusuario)
VALUES('5170e7e806',50, 6, 5);

-- BANCO

INSERT INTO banco(conta, agencia)
VALUES('1093135-X','2624');

INSERT INTO banco(conta, agencia)
VALUES('1191984-1','3628');

INSERT INTO banco(conta, agencia)
VALUES('23635-0','0097');

-- DEPOSITO

INSERT INTO deposito(endereco, valor, idtransacao,bancoconta)
VALUES('5170e7e806',500, 7 ,'1093135-X');

-- CARTEIRA

INSERT INTO carteira(valortotal, idusuario)
VALUES(1000, 2);

INSERT INTO carteira(valortotal, idusuario)
VALUES(1200, 3);

INSERT INTO carteira(valortotal, idusuario)
VALUES(750, 5);

-- CARTEIRA-TRANSACAO

INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
VALUES(80, 4, 1);

INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
VALUES(200, 5, 1);

INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
VALUES(50, 6, 3);

INSERT INTO carteira_transacao(valor, idtransacao,idcarteira)
VALUES(500, 7, 3);
