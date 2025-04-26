from flask import (
    Blueprint, # Organiza o app em partes separadas
    render_template, # Renderiza (mostra) um arquivo HTML na tela 
    redirect, # Manda usuário para outra rota
    url_for, # gera o link correto para uma rota usando o nome da função
    flash, # Cria mensagens rápidas para o usuario (Avisos e erros)
    request # Pega dados enviados pelo usuario
)

from werkzeug.security import (
    generate_password_hash, # Cria uma senha criptografada (Protege senhas antes de salvar no banco)
    check_password_hash # Compara a senha digitada com a senha criptografada (para saber se está correta)
)

from flask_login import (
    login_user, # Loga o usuário (Inicia a sessão dele)
    logout_user, # Desloga o usuário (Encerra a sessão) 
    login_required, # Protege a rota, só deixa acessar se o usuário estiver logado
    current_user # Representa o usuário que está logado no momento
)

from models.user import User, db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        new_user = User(name=name, email=email, password=password) # type:ignore
        db.session.add(new_user)
        db.session.commit()

        flash('Usuário registrado com sucesso')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login realizado!')
            return redirect(url_for('auth.area_protect'))
        else:
            flash('Login inválido')
    
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado!')
    return redirect(url_for('auth.login'))

@auth.route('/area_protect')
@login_required
def area_protect():
    return render_template('home.html', name=current_user.name)
