from flask import Flask, render_template

app = Flask(__name__)

# render_template('home.html'): carrega o arquivo HTML da pasta templates
# {{name}} : isso é Jinja2, ele insere o valor da variavel python no HTML

@app.route('/')
def home():
    name = 'Bruno'
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run(debug=True) 