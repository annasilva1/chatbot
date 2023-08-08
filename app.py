import spacy
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from bardapi import Bard
import os

#Mudar XXXX com os valores de  __Secure-1PSID no f12, application/cookies no site de bardai 
# os.environ['_BARD_API_KEY']="XXXXXXXXX"

#Os dados utilizados abaixo sao com minha chave de acesso por favor preencher com as suas, se for testar muitas vezes.
os.environ['_BARD_API_KEY']="ZQjlvX2O-XmA7_Uw6-hNaqZGBf_97S-X1OdgXH2YoVpmrpA4-j4pg7TRBqDS3ovnR7zAow."
#chaves de acesso acima.


# Criar a instancia de spacy
nlp = spacy.load("en_core_web_sm")

# Criar a instancia de SQLAlchemy
engine = create_engine("sqlite:///weather.db")

# Criando o app 
app = Flask(__name__)

# Definindo as rotas
# Definindo '/'
@app.route("/")
def index():
    return render_template("index.html")

# Definindo `/chat`
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return render_template("chat.html")
    else:
        message = request.form["message"]
        #pegando a mensagem inserida e buscando no bard
        response = Bard().get_answer(message)['content']
        #retornando o campo, com a busca realizada no bard
        return render_template("chat.html", message=message, response=response)
if __name__ == "__main__":
    app.run(debug=True)