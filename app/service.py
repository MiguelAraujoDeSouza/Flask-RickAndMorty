from .database import conecta, encerra_conexao
from MrPoopybuttholeAI import  avaliar_resposta_do_juiz, obter_resposta_da_ia

# Função para mandar mensagem para o banco de dados
def manda_mensagem(mensagem, usuario):
    try:
        conn = conecta()
        cursor = conn.cursor()
        comando = "INSERT INTO mensagens (mensagem, usuario) VALUES (%s,%s);"
        valores = (mensagem, usuario)
        cursor.execute(comando, valores)
        conn.commit()
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao mandar mensagem: {e}")
    finally:
        encerra_conexao(conn)

def manda_mensagem_ia(mensagem):
    try:
        usuarioIA = "IA"
        usuarioJuiz = "Juiz"
        resposta_da_ia = obter_resposta_da_ia(mensagem)
        resposta_do_juiz = avaliar_resposta_do_juiz(mensagem, resposta_da_ia)

        conn = conecta()
        cursor = conn.cursor()

        comando = "INSERT INTO mensagens (mensagem, usuario) VALUES (%s,%s);"
        valores_ia = (resposta_da_ia, usuarioIA)
        cursor.execute(comando, valores_ia)

        valores_juiz = (resposta_do_juiz, usuarioJuiz)
        cursor.execute(comando, valores_juiz)

        conn.commit()
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao mandar mensagem: {e}")
    finally:
        encerra_conexao(conn)


# Função para pegar mensagens do banco de dados
def pegar_mensagens():
    try:
        conn = conecta()
        cursor = conn.cursor()
        comando = "SELECT usuario, mensagem from mensagens order by id_mensagem DESC;"
        cursor.execute(comando)
        acoes = cursor.fetchall()

        listamensagens = []
        for i in range(len(acoes)):
            listamensagens.append(
                f'<font color="black">{acoes[len(acoes) - i - 1][0]}: {acoes[len(acoes) - i - 1][1]}</font>')
        return listamensagens
    except Exception as e:
        print(f"Erro ao pegar mensagens: {e}")
        return []
    finally:
        encerra_conexao(conn)