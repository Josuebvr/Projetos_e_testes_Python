import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host="localhost", database='gerenciador_de_senhas', user='root', password='matrix2003')

    consulta_sql = "select * from tbl_produtos"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os dados cadastrados")
    for coluna in linhas:
        print("Site:", coluna[0])
        print("Login:", coluna[1])
        print("Senha:", coluna[2], "\n")

except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")
