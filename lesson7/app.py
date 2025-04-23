from flask import Flask, request, redirect, url_for, flash, render_template

from flask_login import (
    LoginManager, 
    login_user, 
    login_required, 
    logout_user, 
    UserMixin, 
    current_user) 

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Para sessões e mensagens flash
app.secret_key = 'segredo'

# banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db = SQLAlchemy(app)

# login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # type:ignore

# Model de usuario com login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# view para registro

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        new_user = User(name=name, email=email, password=password) # type: ignore
        db.session.add(new_user)
        db.session.commit()

        flash("Usuario registrado com sucesso")
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
    
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login realizado!")

            return redirect('/area_protect')
        else:
            flash('Login invalido')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout realizado')
    return redirect('/login')

@app.route('/area_protect')
@login_required
def area_protect():
    return render_template('home.html', name=current_user.name)

if __name__ == '__main__':
    app.run(debug=True)