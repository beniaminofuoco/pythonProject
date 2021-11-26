from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Il costruttore prende il nome principale dell'applicazione, che si ottiene con:  __name__
# Se lavoriamo con WTForm dobbiamo inserire OBBLIGATORIAMENTE una chiave segreta per rendere sicura l'applicazione
# questa chiave ci permette di evitare richieste fraudolente al nostro form
app.config["SECRET_KEY"] = "a long and safe secret key"
# URL di connessione al DB
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:juventus@localhost/flaskaskdb'
# Campo consigliato da SQLALCHEMY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Lato Python inizializziamo bootstrap passandogli l'applicazione che stiamo creando
# il restante lavoro viene fatto sui template html
boostrap = Bootstrap(app)
# Inizializzo il DB col costruttore di SQLALCHEMY
db = SQLAlchemy(app)

# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    app.run()  # avvia l'applicazione app