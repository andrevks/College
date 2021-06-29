
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