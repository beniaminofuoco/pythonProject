from flask import Flask
from flask import render_template, redirect
from forms import SignupForm
from models import User

app = Flask(__name__) # Il costruttore prende il nome principale dell'applicazione, che si ottiene con:  __name__

# Se lavoriamo con WTForm dobbiamo inserire OBBLIGATORIAMENTE una chiave segreta per rendere sicura l'applicazione
# questa chiave ci permette di evitare richieste fraudolente al nostro form
app.config["SECRET_KEY"] = "a long and safe secret key"


# methods ci permtte di specificare il tipo di richiesta, di default è GET, nel nostro caso ci serve fare una POST
@app.route('/', methods=['GET', 'POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        return render_template('profile.html', user=user)

    return render_template('signup.html', form=form)


# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    app.run()  # avvia l'applicazione app