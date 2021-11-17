from flask import Flask

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
        return "<h1>Forbidden</h1>", 403
    return "Hello "+user+"!", 200

# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    print(app.url_map) # Stampa il numero delle Route che abbiamo creato all'interno dell'app
    app.run() # avvia l'applicazione app