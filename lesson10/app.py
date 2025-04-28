from flask import Flask, request, flash, redirect, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'media')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'minha_chave_secreta'  # Adicionado para o flash funcionar

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload/', methods=['GET', 'POST']) 
def upload():
    if request.method == 'POST':
        file = request.files['file']
        
        if file.filename == '':
            flash('Nenhum arquivo selecionado.')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename or '')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Arquivo salvo com sucesso.')
            return redirect('/upload')  # Redireciona para a própria página ou outra rota
        
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
