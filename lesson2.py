from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página Inicial'

# EX: http://127.0.0.1:5000/user/bruno
@app.route('/user/<name>')
def user(name):
    return f'Olá, {name.capitalize()}!'

# EX: http://127.0.0.1:5000/age/22
@app.route('/age/<int:age>')
def user_age(age):
    return f'Você tem {age} anos.'

if __name__ == '__main__':
    app.run(debug=True) 