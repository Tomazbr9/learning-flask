from flask import Flask, abort, render_template, request, redirect

from flask_login import login_required, UserMixin, current_user, LoginManager, login_user

from flask_sqlalchemy import SQLAlchemy

from functools import wraps

app = Flask(__name__)

app.secret_key = 'segredo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # type:ignore

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

@login_manager.user_loader # type:ignore
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        new_user = User(name=name, password=password) # type:ignore
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()
        
        if user and user.password == password:
            login_user(user)
            return redirect('/home')
        else:
            abort(403)
    
    return render_template('login.html')

@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    
    if request.method == 'POST':
        
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()
        
        if user and user.password == password:
            login_user(user)
            return redirect('/admin')
        else:
            abort(403)
    
    return render_template('admin_form.html')


@app.route('/admin')
@admin_required
def admin_dashboard():
    return render_template('admin.html')

@login_required
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)