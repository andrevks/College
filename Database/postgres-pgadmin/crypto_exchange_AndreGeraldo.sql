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
  valor NUMERIC(10,9) NOT NULL,
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
  valor NUMERIC(10,9) NOT NULL,
  idtransacao INTEGER NOT NULL,
  bancoconta CHAR NOT NULL,
  CONSTRAINT pkdeposito PRIMARY KEY (iddeposito),
  CONSTRAINT fkdeposito_transacao FOREIGN KEY (idtransacao) REFERENCES trasacao(idtransacao),
  CONSTRAINT fkdeposito_bancoconta FOREIGN KEY (bancoconta) REFERENCES banco(conta)
);

CREATE TABLE saque (
  idsaque SERIAL NOT NULL,
  endereco VARCHAR(30) NOT NULL,
  valor NUMERIC(10,9) NOT NULL,
  idtransacao INTEGER NOT NULL,
  idusuario INTEGER NOT NULL,
  CONSTRAINT pksaque PRIMARY KEY (idsaque),
  CONSTRAINT fksaque_transacao FOREIGN KEY (idtransacao) REFERENCES trasacao(idtransacao),
  CONSTRAINT fksaque_usuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE carteira (
  idcarteira SERIAL NOT NULL,
  valortotal NUMERIC(10,9) NOT NULL,
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