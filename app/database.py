import psycopg2
import os
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()

def conecta():
    try:
        conn = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password= os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        print("Conectado no postgres com sucesso!!")
        return conn
    except Error as e:
        print(f"Ocorreu um erro ao tentar conectar no banco de dados: {e}")

def encerra_conexao(conn):
    if conn:
        conn.close()
        print("Conexão encerrada com o banco de dados!")