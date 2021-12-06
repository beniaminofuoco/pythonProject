from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from flask import current_app
from enum import Enum

class ConfirmResult(Enum):
    CONFIRMED = 1
    ALREADY_CONFIRMED = 2
    INVALID_TOKEN = 3

# Estendiamo la classe UserMixIn
class User(UserMixin, db.Model):

    # Con questa istruzione andiamo a dire che per il Model USer verrà creata la tabella 'users' sul DB
    __tablename__ = 'users'

    # Definizione dei vari campi nella tabella 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    # Rendo privato il metodo get per ottenere la password
    @property
    def password(self):
        raise AttributeError("Password is not readable attribute")

    # Utilizzo il metodo set per salvare la password dopo averne fatto l'hash
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # faccio il confronto tra la password inserita e quella presente a DB
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    # Funzione statica, infatti non compare il classico "self"
    def confirm(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads((token.encode('utf-8')))
        except:
            return ConfirmResult.INVALID_TOKEN
        uid = data.get('confirm')
        user = User.query.get(uid)

        if not user:
            return ConfirmResult.INVALID_TOKEN

        if user.confirmed:
            return ConfirmResult.ALREADY_CONFIRMED

        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        return ConfirmResult.CONFIRMED


User.confirm = staticmethod(User.confirm)

# Da console Python
# from main import db
# from models import User
# db.create_all()
# user = User(email="ben.fuo@pippo.it", username="b.fuoco", password="123456")
# db.session.add(user)
# db.session.commit()

# Aggiungo più utenti in un unico commit
# user2 = User(email="benia.fuo@pippo.it", username="be.fuoco", password="123456")
# user3 = User(email="beniami.fuo@pippo.it", username="benia.fuoco", password="123456")
# db.session.add_all(user2, user3)
# db.session.add_all([user2, user3])
# db.session.commit()

# Modifico l'username di user2
# user2.username = "f.be"
# db.session.add(user2)
# db.session.commit()

# Cancelliamo uno user
# db.session.delete(user2)
# db.session.commit()

# Query sul DB
# Query -> User.query.all()
# Result [<User 1>, <User 3>]

# Iteriamo sul risultato e stampiamo username
# for user in User.query.all():
#     print(user.username)
#
# b.fuoco
# benia.fuoco


# Per filtrare utilizzo il metodo filter_by
# (all() restituisce tutti gli elementi che soddisfano la condizione di filtro)
# User.query.filter_by(email="ben.fuo@pippo.it").all()
# [<User 1>]
# (first () solo il primo elemento che soddisfa la condizione di filtro)
# User.query.filter_by(email="ben.fuo@pippo.it").first()
# <User 1>


# Per cancellare tutte le righe di una tabella
# User.query.delete()
# 2 (numero di righe cancellate)
# db.session.commit()

# Se vogliamo cancellare l'intero contenuto del del db
#