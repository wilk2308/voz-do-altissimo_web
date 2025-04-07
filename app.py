from flask import Flask, render_template, request
from gerar_resposta import gerar_resposta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        mensagem = request.form["mensagem"]
        resposta = gerar_resposta(mensagem)
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
