from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from ProjectBlogJeff.models import Usuario
from flask_login import current_user

class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(4, 10)])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido')])
    senha_create = PasswordField('Digite sua senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Digite sua senha novamente', validators=[DataRequired(), EqualTo('senha_create', message='Senha Esta Diferente.')])
    botao_submit_criar_conta = SubmitField('Criar Conta')

    def validate_email(self, email):
        verificacao = Usuario.query.filter_by(email=email.data).first()
        if verificacao:
            raise ValidationError('E-mail ja cadastrado. Cadastre-se com um novo e-mail ou faça login.')

    def validate_username(self, username):
        verificacao = Usuario.query.filter_by(username=username.data).first()
        if verificacao:
            raise ValidationError('Nome de usuario já cadastrado.')

class FormLoginAccount(FlaskForm):
    email_login = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail Inválido. Digite novamente')])
    senha_login = PasswordField('Digite a senha', validators=[DataRequired()])
    lembrar_dados = BooleanField('Lembrar Dados de Acessos')
    botao_submit_entrar = SubmitField('Entrar')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(4, 10)])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido')])
    botao_submit_editar_perfil = SubmitField('Editar Perfil')
    nova_foto_perfil = FileField('Foto de perfil', validators=[FileAllowed(['jpg', 'png'], message='''Extensão do arquivo
                                                                                                   inválida. Escolha
                                                                                                   (JPG OU PNG).''')])

    curso_excel = BooleanField('Excel')
    curso_python = BooleanField('Python')
    curso_sql = BooleanField('Banco de Dados SQL')
    curso_powerbi = BooleanField('Power BI')

    def validate_username(self, username):
        if current_user.username != username.data:
            usuario = Usuario.query.filter_by(username=username.data).first()
            if usuario:
                raise ValidationError('Nome de usuário já esta em uso.')
    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail ja esta em uso. Informe um e-mail válido.')


class CriarPost(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    corpo = TextAreaField('Postagem', validators=[DataRequired()])
    botao_submit = SubmitField('Postar')