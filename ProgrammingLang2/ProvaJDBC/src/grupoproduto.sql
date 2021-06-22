CREATE TABLE grupoproduto(
    codigo serial NOT NULL,
    nome character(40) NOT NULL,
    promocao numeric(5,2),
    margemlucro numeric(5,2),
    PRIMARY KEY(codigo)
);