import psycopg2
import os
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()

# Conexão com o banco de dados PostgreSQL
def conecta():
    try:
        conn = psycopg2.connect(
            user=os.getenv("user"),
            password= os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            database=os.getenv("database")
        )
        print("Conectado no postgres com sucesso!!")
        return conn
    except Error as e:
        print(f"Ocorreu um erro ao tentar conectar no banco de dados: {e}")

# Função para encerrar a conexão com o banco de dados
def encerra_conexao(conn):
    if conn:
        conn.close()
        print("Conexão encerrada com o banco de dados!")