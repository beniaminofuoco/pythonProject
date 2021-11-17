from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/user/<user>')
def hello_user(user):
    return render_template("user.html", user=user)

@app.route('/list/<user>')
def hello_list(user):
    user_info_py = ["Age=37", "Gender=male", "Height=1cm", "Weigth=81kg"]
    # il primo parametro in rosso deve coincidere con quello presente nel template html
    # se non passiamo la variabile 'user' si entrerà nel caso 'else' del template
    return render_template("user_info.html", user=user, user_info=user_info_py)

if __name__ == '__main__':
    app.run()  # avvia l'applicazione app