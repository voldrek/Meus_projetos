CREATE DATABASE APP_PIZZARIA;
USE APP_PIZZARIA;

-- Criando tabela CADASTRO_FUNCIONARIOS
CREATE TABLE CADASTRO_FUNCIONARIO (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    NOME VARCHAR (255) NOT NULL,
    CARGO VARCHAR (255) NOT NULL,
    SENHA VARCHAR (255) NOT NULL,
	SALARIO INT NOT NULL,
	HORARIO varchar(255) NOT NULL,
	EMAIL VARCHAR (255) NOT NULL,
);

-- Criando tabela FUNCIONARIOS com chave estrangeira para CADASTRO_FUNCIONARIOS
CREATE TABLE FUNCIONARIOS (
    ID INT PRIMARY KEY,  -- Chave estrangeira para CADASTRO_FUNCIONARIOS
    NOME VARCHAR(255) NOT NULL,
    CARGO VARCHAR(255) NOT NULL,
    SALARIO INT NOT NULL,
	 HORARIO VARCHAR(255) NOT NULL,
	EMAIL VARCHAR (255) NOT NULL,
    FOREIGN KEY (ID) REFERENCES CADASTRO_FUNCIONARIO(id)
);


-- Criando o trigger para inserir automaticamente na tabela FUNCIONARIOS
CREATE TRIGGER tr_CadastroFuncionarios_Insert
ON CADASTRO_FUNCIONARIO
AFTER INSERT
AS
BEGIN
    INSERT INTO FUNCIONARIOS (ID, NOME, CARGO, HORARIO, SALARIO , EMAIL)
    SELECT ID, NOME, CARGO, HORARIO, SALARIO , EMAIL
    FROM INSERTED;
END;


-- Inserindo dados na tabela CADASTRO_FUNCIONARIOS
INSERT INTO CADASTRO_FUNCIONARIO (NOME, CARGO, SENHA, SALARIO, HORARIO , EMAIL)
VALUES ('LUCAS DA SILVA JORDANO', 'CHEFE', '123', 1500, '8:00 as 18:00', 'LUCASJORDANO@GMAIL.COM');

INSERT INTO CADASTRO_FUNCIONARIO (NOME, CARGO, SENHA, SALARIO, HORARIO , EMAIL)
VALUES ('ANDRESSA GILIOLI DO CARMOS SILVA', 'CHEFE', '123', 1500, '8:00 as 18:00','ANDRESSAGILIOLI@GMAIL.COM');

-- Verificando a tabela FUNCIONARIOS
SELECT * FROM CADASTRO_FUNCIONARIO;
SELECT * FROM FUNCIONARIOS;


-- Excluindo a tabela FUNCIONARIOS (opcional)
DROP TABLE FUNCIONARIOS;
DROP TABLE CADASTRO_FUNCIONARIO;
----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Produtos--------------------------------------------------------------------------

-- Criando tabela CADASTRO_FUNCIONARIOS
CREATE TABLE PRODUTOS (
    ID INT IDENTITY (1,1) PRIMARY KEY,
	NOME_PRODUTO VARCHAR(255),
	CATEGORIA VARCHAR(255),
	PRECO_PRODUTO VARCHAR(255)
);



SELECT * FROM PRODUTOS;
DROP TABLE PRODUTO;
DROP TABLE CADASTRO_PRODUTO;

DELETE FROM CADASTRO_PRODUTO
WHERE ID = 149;       

----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Clientes--------------------------------------------------------------------------             
CREATE TABLE CLIENTES (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    NOME VARCHAR(255) NOT NULL,
    ENDERECO VARCHAR(255),
    TELEFONE VARCHAR(20)
);

-- Adicionando uma coluna CLIENTE_ID na tabela de PEDIDOS
ALTER TABLE PEDIDOS
ADD CLIENTE_ID INT;

-- Vinculando os pedidos aos clientes pelo ID do cliente
UPDATE PEDIDOS
SET CLIENTE_ID = (SELECT ID FROM CLIENTES WHERE NOME = 'Nome do Cliente');

-- Exemplo de inser��o de cliente
INSERT INTO CLIENTES (NOME, ENDERECO, TELEFONE)
VALUES ('Nome do Cliente', 'Endere�o do Cliente', 'Telefone do Cliente');    

----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Endere�os--------------------------------------------------------------------------                  

-- Criando tabela de ENDERE�OS
CREATE TABLE ENDERECOS (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    CLIENTE_ID INT NOT NULL,  -- Chave estrangeira para o cliente
    RUA VARCHAR(255) NOT NULL,
    NUMERO VARCHAR(10) NOT NULL,
    BAIRRO VARCHAR(100),
    CIDADE VARCHAR(100),
    ESTADO VARCHAR(100),
    CEP VARCHAR(10)
);

-- Adicionando a chave estrangeira para vincular os endere�os aos clientes
ALTER TABLE ENDERECOS
ADD CONSTRAINT FK_CLIENTE_ENDERECO
FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTES(ID);
                                                                 
----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Pedidos--------------------------------------------------------------------------


-- Criando tabela PEDIDOS
CREATE TABLE PEDIDOS (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    CLIENTE_ID INT NOT NULL,  -- Chave estrangeira para o cliente
    DATA_PEDIDO DATE NOT NULL,
    STATUS_PEDIDO VARCHAR(50) NOT NULL,
    VALOR_TOTAL DECIMAL(10, 2) NOT NULL,
    
    FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTES(ID)
);


----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Hist�rico de pedidos--------------------------------------------------------------------------
-- Criando tabela de HISTORICO_PEDIDOS
CREATE TABLE HISTORICO_PEDIDOS (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    CLIENTE_ID INT NOT NULL,  -- Chave estrangeira para o cliente
    PEDIDO_ID INT NOT NULL,   -- Chave estrangeira para o pedido
    DATA_PEDIDO DATE NOT NULL,
    VALOR_TOTAL DECIMAL(10, 2) NOT NULL,
    
    -- Outros campos relevantes sobre o pedido (por exemplo, status, observa��es, etc.)
    
    FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTES(ID),
    FOREIGN KEY (PEDIDO_ID) REFERENCES PEDIDOS(ID)
);                                              


----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Status dos pedidos--------------------------------------------------------------------------



-- Criar tabela para STATUS DOS PEDIDOS
CREATE TABLE STATUS_PEDIDO (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    NOME_STATUS VARCHAR(50) NOT NULL
);         

-- Inserir status dos pedidos
INSERT INTO STATUS_PEDIDO (NOME_STATUS)
VALUES ('Pendente');

INSERT INTO STATUS_PEDIDO (NOME_STATUS)
VALUES ('Em Prepara��o');

INSERT INTO STATUS_PEDIDO (NOME_STATUS)
VALUES ('Entregue');

-- Adicionar coluna STATUS_ID � tabela HISTORICO_PEDIDOS
ALTER TABLE HISTORICO_PEDIDOS
ADD STATUS_ID INT;

-- Adicionar chave estrangeira para vincular os pedidos aos status
ALTER TABLE HISTORICO_PEDIDOS
ADD CONSTRAINT FK_STATUS_PEDIDO
FOREIGN KEY (STATUS_ID) REFERENCES STATUS_PEDIDO(ID);         

----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Pagamento--------------------------------------------------------------------------

-- Criando tabela PAGAMENTOS
CREATE TABLE PAGAMENTOS (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    CLIENTE_ID INT NOT NULL,  -- Chave estrangeira para o cliente
    METODO_PAGAMENTO VARCHAR(50) NOT NULL,  -- Coluna para registrar o m�todo de pagamento
    VALOR_TOTAL DECIMAL(10, 2) NOT NULL,
    DATA_PAGAMENTO DATETIME NOT NULL,
    NUMERO_CARTAO VARCHAR(20),  -- N�mero do cart�o de cr�dito
    NOME_TITULAR_CARTAO VARCHAR(255),  -- Nome do titular do cart�o de cr�dito
    DATA_VENCIMENTO_CARTAO DATE,  -- Data de vencimento do cart�o de cr�dito
    RECEIPT_URL VARCHAR(255),  -- URL do recibo ou comprovante de pagamento
    
    FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTES(ID)
);


----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Promo��es--------------------------------------------------------------------------
-- Criando tabela PROMOCOES
CREATE TABLE PROMOCOES (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    NOME_PROMOCAO VARCHAR(255) NOT NULL,
    DESCRICAO_PROMOCAO VARCHAR(500),
    VALOR_DESCONTO DECIMAL(10, 2),
    TIPO_DESCONTO VARCHAR(50),  -- Porcentagem ou valor fixo
    DATA_INICIO DATETIME,
    DATA_FIM DATETIME
);

-- Criando tabela PEDIDOS_PROMOCOES para associar pedidos a promo��es
CREATE TABLE PEDIDOS_PROMOCOES (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    PEDIDO_ID INT NOT NULL,  -- Chave estrangeira para o pedido
    PROMOCAO_ID INT NOT NULL,  -- Chave estrangeira para a promo��o
    
    FOREIGN KEY (PEDIDO_ID) REFERENCES PEDIDOS(ID),
    FOREIGN KEY (PROMOCAO_ID) REFERENCES PROMOCOES(ID)
);
                                     

----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------Avalia��es--------------------------------------------------------------------------
-- Criando tabela AVALIACOES
CREATE TABLE AVALIACOES (
    ID INT IDENTITY (1,1) PRIMARY KEY,
    CLIENTE_ID INT NOT NULL,  -- Chave estrangeira para o cliente
    PEDIDO_ID INT NOT NULL,   -- Chave estrangeira para o pedido
    NOTA INT,                -- Nota ou classifica��o (por exemplo, de 1 a 5)
    COMENTARIO TEXT,         -- Coment�rio ou feedback do cliente
    DATA_AVALIACAO DATETIME  -- Data e hora da avalia��o
);

-- Criando chaves estrangeiras para associar avalia��es a clientes e pedidos
ALTER TABLE AVALIACOES
ADD CONSTRAINT FK_AVALIACAO_CLIENTE
FOREIGN KEY (CLIENTE_ID) REFERENCES TABELA_DE_CLIENTES(ID);

ALTER TABLE AVALIACOES
ADD CONSTRAINT FK_AVALIACAO_PEDIDO
FOREIGN KEY (PEDIDO_ID) REFERENCES PEDIDOS(ID);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              