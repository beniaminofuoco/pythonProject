from main import db

class User(db.Model):

    # Con questa istruzione andiamo a dire che per il Model USer verrà creata la tabella 'users' sul DB
    __tablename__ = 'users'

    # Definizione dei vari campi nella tabella 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))


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