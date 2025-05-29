from .database import conecta, encerra_conexao


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


def pegar_mensagens():
    try:
        conn = conecta()
        cursor = conn.cursor()
        comando = "SELECT usuario, mensagem from mensagens order by id_mensagem;"
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