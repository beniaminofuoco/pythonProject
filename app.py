from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__) # Il costruttore prende il nome principale dell'applicazione, che si ottiene con:  __name__
# Se lavoriamo con WTForm dobbiamo inserire OBBLIGATORIAMENTE una chiave segreta per rendere sicura l'applicazione
# questa chiave ci permette di evitare richieste fraudolente al nostro form
app.config["SECRET_KEY"] = "a long and safe secret key"
# URL di connessione al DB
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:juventus@localhost/flaskaskdb'
# Campo consigliato da SQLALCHEMY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configurazione EMAIL
app.config['MAIL_SERVER'] = 'server111.web-hosting.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'flaskask@alienconcept.co'
app.config['MAIL_USERNAME'] = 'flaskask@alienconcept.co'
app.config['MAIL_PASSWORD'] = 'UFHShRgU3jCdrBT'

# Lato Python inizializziamo bootstrap passandogli l'applicazione che stiamo creando
# il restante lavoro viene fatto sui template html
boostrap = Bootstrap(app)
# Inizializzo il DB col costruttore di SQLALCHEMY
db = SQLAlchemy(app)
# Configurazione di flask Migrate
migrate = Migrate(app, db)

# Configurazione della mail nella nostra app
mail = Mail(app)

# Configuriamo LoginManager
login_manager = LoginManager(app)
# Dobbiamo anche specificare un valore per login_view per indirizzare un utente non autorizzato.
# il valore "login" utilizzando i decoratori è il nome della "url" a cui vogliamo indirizzare l'utente.
login_manager.login_view = "login"


# riferimento ai models da inserire dopo la configurazione di migrate
# importiamo i modelli e le views che verranno utilizzati dall'app
from models import *
from views import *

# il decoratore @login_manager indica alla libreria l'utente da carica
# il parametro è passato come stringa, la funzione int lo trasforma in intero da utilizzare nella query
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# Migrate (rinominare il file main con app.py)
# flask db init
# flask db migrate -m "first migrate"
# flask db upgrade (aggiorna il mio DB postgres con il file di version creato dai comandi precedenti)
# Migrate è utile quando ci sono delle piccole modifiche al model e non ci sono tanti dati sul DB

# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    app.run()  # avvia l'applicazione app