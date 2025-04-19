from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# methods=['POST'] : envia dados de forma segura
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name'] # pega dados do input chamado 'name'
    return render_template('result.html', name=name) # name=name dado é passado
                                                     # para o HTML
if __name__ == '__main__':
    app.run(debug=True) 