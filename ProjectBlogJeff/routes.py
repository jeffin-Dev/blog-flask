from flask import render_template, url_for, request, flash, redirect, abort
from ProjectBlogJeff.forms import FormLoginAccount, FormCreateAccount, FormEditarPerfil, CriarPost, EditarPost
from ProjectBlogJeff import app, database, bcrypt
from ProjectBlogJeff.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
from ProjectBlogJeff.funcoes import tratamento_img, validar_cursos, cursos_lista


@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())

    return render_template('home.html', posts=posts)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    cursos = cursos_lista(current_user.cursos)
    qtd_cursos = len(cursos)
    return render_template('usuarios.html', lista_usuarios=lista_usuarios, qtd_cursos=qtd_cursos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLoginAccount()
    form_create_account = FormCreateAccount()
    if form_login.validate_on_submit() and 'botao_submit_entrar' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email_login.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha_login.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Boas vindas, {form_login.email_login.data}.', 'alert-success')
            parametro_next = request.args.get('next')
            if parametro_next:
                return redirect(parametro_next)
            else:
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
@login_required
def logout():
    logout_user()
    flash('Deslogado Com Sucesso.', 'alert-success')
    return redirect(url_for('login'))

@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form = CriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Sua publicação foi postada.','alert-success')
        return redirect(url_for('home'))
    return render_template('criar_post.html', form=form)

@app.route('/perfil')
@login_required
def meu_perfil():
    form_editar_perfil = FormEditarPerfil()
    foto_perfil = url_for('static', filename= 'fotos_perfil/{}'.format(current_user.foto_de_perfil))
    cursos = cursos_lista(current_user.cursos)
    qtd_cursos = len(cursos)
    return render_template('meu_perfil.html', foto_perfil=foto_perfil,
                           form_editar_perfil=form_editar_perfil, cursos=cursos, qtd_cursos=qtd_cursos)

@app.route('/editar-perfil', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form_editar_perfil = FormEditarPerfil()
    if form_editar_perfil.validate_on_submit():
        if form_editar_perfil.nova_foto_perfil.data:
            nome_img = tratamento_img(form_editar_perfil.nova_foto_perfil.data)
            current_user.foto_de_perfil = nome_img
        current_user.email = form_editar_perfil.email.data
        current_user.username = form_editar_perfil.username.data
        current_user.cursos = validar_cursos(form_editar_perfil)
        database.session.commit()
        flash('Perfil Atualizado com Sucesso.', 'alert-success')
        return redirect(url_for('meu_perfil'))
    elif request.method == 'GET':
        form_editar_perfil.email.data = current_user.email
        form_editar_perfil.username.data = current_user.username

    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_de_perfil))
    return render_template('editar_perfil.html', foto_perfil=foto_perfil,
                           form_editar_perfil=form_editar_perfil)


@app.route('/post/<id_post>', methods=['GET', 'POST'])
def post_usuario(id_post):
    post = Post.query.get(id_post)
    if current_user == post.autor:
        editar = EditarPost()
        if request.method == 'GET':
            editar.titulo.data = post.titulo
            editar.corpo.data = post.corpo
        elif editar.validate_on_submit():
            post.titulo = editar.titulo.data
            post.corpo = editar.corpo.data
            database.session.commit()
            flash('Post Atualizado.', 'alert-success')
            return redirect(url_for('home'))
    else:
        editar = None
    return render_template('post_usuario.html', post=post, editar=editar)

@app.route('/post/<id_post>/excluir', methods=['GET', 'POST'])
@login_required
def excluir_post(id_post):
    post = Post.query.get(id_post)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Postagem Excluida', 'alert-danger')
        return redirect(url_for('home'))
    else:
        abort(403)
    return render_template('post_usuario.html', id_post=id_post)