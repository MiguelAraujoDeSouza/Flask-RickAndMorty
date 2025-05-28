from flask import Blueprint, render_template, request, redirect, url_for
from .service import manda_mensagem, pegar_mensagens
bp = Blueprint("chat", __name__)

@bp.route("/health", methods=["GET"])
def health():
    return "OK", 200


@bp.route("/", methods=["GET", "POST"])
def home():
    global nick
    if request.method == "POST":
        nick = request.form["user"]
        print(nick)
    return render_template("index.html")

@bp.route("/usuario", methods=["GET", "POST"])
def usuario():
    if request.method == "POST":
        manda_mensagem(request.form["mensagem"], str(nick))
        return redirect(url_for("chat.usuario"))
    elif request.method == "GET":
        mensagens = pegar_mensagens()
        return render_template("usuario.html", historico=mensagens)