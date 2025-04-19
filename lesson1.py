from flask import Flask

# Cria aplicação 
app = Flask(__name__)

# Definine a rota para o caminho '/' (pagina inicial)
@app.route('/')
def home():
    return 'Olá Flask'

if __name__ == '__main__':
    app.run(debug=True) # degug=True : permite recarregar o servidor
                        # automaticamente em alterações de código