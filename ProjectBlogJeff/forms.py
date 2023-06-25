from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from ProjectBlogJeff.models import Usuario


class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(4, 10)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha_create = PasswordField('Digite sua senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Digite sua senha novamente', validators=[DataRequired(), EqualTo('senha_create')])
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
    email_login = StringField('E-mail', validators=[DataRequired(), Email()])
    senha_login = PasswordField('Digite sua senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acessos')
    botao_submit_entrar = SubmitField('Entrar')

