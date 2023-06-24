from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(4, 10)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha_create = PasswordField('Digite sua senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Digite sua senha novamente', validators=[DataRequired(), EqualTo('senha_create')])
    botao_submit_criar_conta = SubmitField('Criar Conta')


class FormLoginAccount(FlaskForm):
    email_login = StringField('E-mail', validators=[DataRequired(), Email()])
    senha_login = PasswordField('Digite sua senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acessos')
    botao_submit_entrar = SubmitField('Entrar')

