from flask import Flask

app = Flask(__name__) # Il costruttore prende il nome principale dell'applicazione, che si ottiene con:  __name__

# view function, cioe' il codice che viene eseguito quando richiamimo la route
def hello():
    return "Hello Flask!"

# creiamo la route
# il metodo prende 3 parametri:
# 1) l'url che vogliamo chiamare (in questo caso la nostra index)
# 2) il path che identifica la nostra route
# 3) la view function che sarà eseguita quando richiamiamo la route
app.add_url_rule("/", "hello", hello)

# Questo costrutto ci dice che il codice verra' eseguito solo se viene lanciato lo script manualmente (e non importato)
if __name__ == '__main__':
    app.run() # avvia l'applicazione app