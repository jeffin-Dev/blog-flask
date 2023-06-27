from flask import render_template, url_for, request, flash, redirect
from ProjectBlogJeff.forms import FormLoginAccount, FormCreateAccount
from ProjectBlogJeff import app, database, bcrypt
from ProjectBlogJeff.models import Usuario
from flask_login import login_user, logout_user, current_user

lista_usuarios = ['Jeff', 'Isa', 'João', 'Pedro', 'Ana']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLoginAccount()
    form_create_account = FormCreateAccount()
    if form_login.validate_on_submit() and 'botao_submit_entrar' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email_login.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha_login.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Boas vindas, {form_login.email_login.data}.', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash('E-mail ou Senha Incorreta. Verifique e tente novamente', 'alert-danger')
    if form_create_account.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        pass_cript = bcrypt.generate_password_hash(form_create_account.senha_create.data)
        usuario = Usuario(username=form_create_account.username.data, email=form_create_account.email.data,
                          senha=pass_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Boas vindas {form_create_account.username.data}.', 'alert alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_create_account=form_create_account)

@app.route('/sair')
def logout():
    logout_user()
    flash('Deslogado Com Sucesso.', 'alert-success')
    return redirect(url_for('login'))

@app.route('/post/criar')
def criar_post():
    return render_template('criar_post.html')

@app.route('/perfil')
def meu_perfil():
    return render_template('meu_perfil.html')