from flask import Blueprint, render_template, request, redirect, url_for
from .service import manda_mensagem, pegar_mensagens, manda_mensagem_ia, apagar_mensagens
bp = Blueprint("chat", __name__)

# Rota para verificar a saúde da API
@bp.route("/health", methods=["GET"])
def health():
    return "OK", 200

# Rota para pegar o nick do usuario
@bp.route("/", methods=["GET", "POST"])
def home():
    global nick
    if request.method == "POST":
        nick = request.form["user"]
        print(nick)
    return render_template("index.html")

# Rota para o chat do usuário
@bp.route("/usuario", methods=["GET", "POST"])
def usuario():
    ## n tem metodo delete ent tive que improvisar no postkkkkkk 
    if request.method == "POST":
        print(request.form["mensagem"])
        if request.form["mensagem"] == "Limpar mensagens":
            apagar_mensagens()
            return redirect(url_for("chat.usuario"))
        else:
            manda_mensagem(request.form["mensagem"], str(nick))
            return redirect(url_for("chat.usuario"))
    elif request.method == "GET":
        mensagens = pegar_mensagens()
        return render_template("usuario.html", historico=mensagens)