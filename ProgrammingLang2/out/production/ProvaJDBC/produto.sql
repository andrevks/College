CREATE TABLE produto (
    codigo SERIAL NOT NULL,
    nome CHARACTER(50) NOT NULL,
    estoque INTEGER,
    valorcompra NUMERIC(10,2),
    promocao NUMERIC(5,2),
    margemlucro NUMERIC(5,2),
    grupo INTEGER NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (grupo) REFERENCES grupoproduto(codigo)
);