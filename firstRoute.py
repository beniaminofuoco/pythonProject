from flask import Flask

# Questo file ci mostra come creare delle Route utilizzando add_url_route
# più avanti vedremo come creare le stesse route usando i decoratori

app = Flask(__name__) # Il costruttore prende il nome principale dell'applicazione, che si ottiene con:  __name__

# view function, cioe' il codice che viene eseguito quando richiamimo la route
def hello():
    return "Hello Flask!"

def bye():
    return "<h1> By Flask! </h1>" \
            "<p> Hope to see you again soon </p>"


# creiamo la route con add_url_route
# il metodo prende 3 parametri:
# 1) l'url che vogliamo chiamare (in questo caso la nostra index)
# 2) identificativo che identifica la nostra route nell'app
# 3) la view function che sarà eseguita quando richiamiamo la route
app.add_url_rule("/", "hello", hello)
# il primo parametro e' una URL e deve iniziare sempre con /
app.add_url_rule("/bye", "bye", bye)


# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    print(app.url_map) # Stampa il numero delle Route che abbiamo creato all'interno dell'app
    app.run() # avvia l'applicazione app