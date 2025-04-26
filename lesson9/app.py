from flask import Flask, redirect, render_template, flash
from forms import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'segredo'

from forms import RegisterForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # validate_on_submit faz todas a verificação
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        print(name)
        print(email)
        print(password)

        flash("Usuário registrado com sucesso!")
        return redirect('home.html')
    
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)