import mysql.connector

try:
    # Criar conexão ao banco de dados
    con = mysql.connector.connect(
        host="localhost", database='gerenciador_de_senhas', user='root', password='matrix2003')

    # Declaração SQL a ser executada
    criar_tabela_SQL = """CREATE TABLE tbl_produtos (
                            IdProduto int(11) NOT NULL,
                            NomeProduto VARCHAR(70) NOT NULL,
                            Preco FLOAT NOT NULL,
                            Quantidade TINYINT NOT NULL,
                            PRIMARY KEY (IdProduto)) """
    # Criar cursor e executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de Senhas criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada.")
