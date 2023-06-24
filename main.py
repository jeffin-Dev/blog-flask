from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCreateAccount, FormLoginAccount
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


lista_usuarios = ['Jeff', 'Isa', 'João', 'Pedro', 'Ana']
app.config['SECRET_KEY'] = 'd24f396f2a891195866947f4df0e1e96'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

database = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contatos')
def contato():
    return render_template('contato.html')

@app.route('/usuario')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLoginAccount()
    form_create_account = FormCreateAccount()

    if form_login.validate_on_submit() and 'botao_submit_entrar' in request.form:
        flash(f'Boas vindas, {form_login.email_login.data}.', 'alert-success')
        return redirect(url_for('home'))

    if form_create_account.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        flash(f'Boas vindas {form_create_account.username.data}.', 'alert alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_create_account=form_create_account)



if __name__ == '__main__':
    app.run(debug=True)