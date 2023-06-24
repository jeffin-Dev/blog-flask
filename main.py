from flask import Flask, render_template, url_for

app = Flask(__name__)


lista_usuarios = ['Jeff', 'Isa', 'João', 'Pedro', 'Ana']


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contatos')
def contato():
    return render_template('contato.html')

@app.route('/usuario')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/criar_conta')
def criar_conta():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)