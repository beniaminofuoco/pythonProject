from flask import Flask
from flask import abort, redirect
from flask import request

app = Flask(__name__) # Il costruttore prende il nome principale dell'applicazione, che si ottiene con:  __name__

# Il decoratore e' un design pattern che viene utilizzato per estendere le
# funzionalita di una funzione o di un metodo senza modificarne la struttura

# Il decoratore inizia sempre con una @
# rispetto alle route create con add_url_route abbiamo un parametro in meno: la route
# con i decoratori la route corrisponde al nome della funzione

# view function, cioe' il codice che viene eseguito quando richiamimo la route
@app.route('/')
def hello():
    return "Hello Flask!"

@app.route('/bye')
def bye():
    return "<h1> By Flask! </h1>" \
            "<p> Hope to see you again soon </p>"

# Definiamo una route dinamica, dove passiamo un paremtro alla route
# Il parametro viene passato nel decoratore tramite parentesi angolari <>
# e come parametro nella funzione hello_user
@app.route('/user/<user>')
def hello_user(user):
    if user != "beniamino":
        abort(403)  # come vediamo non c'è bisogno del return
    return redirect("http://google.com")

@app.route('/info')
def info():
    info_list = "<ul>"  # questo tag crea una list di elementi, il tag li crea un elemento della lista
    info_list += "<li>User-Agent= "+request.headers.get('User-Agent')+"</li>"  # User Agent
    info_list += "<li>User IP= "+request.remote_addr+"</li>"  # indirizzo IP di chi si sta collegando

    for env_info in request.environ:
        info_list += "<li>"+env_info+" = "+str(request.environ[env_info])+"</li>"

    info_list += "</ul>"

    return  info_list


# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    print(app.url_map)  # Stampa il numero delle Route che abbiamo creato all'interno dell'app
    app.run()  # avvia l'applicazione app