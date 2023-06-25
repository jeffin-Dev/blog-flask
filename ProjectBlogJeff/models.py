from ProjectBlogJeff import database
from datetime import datetime


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(10), nullable=False, unique=True)
    email = database.Column(database.String, unique=True, nullable=False)
    senha = database.Column(database.String, nullable=False)
    foto_de_perfil = database.Column(database.String, nullable=False, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_de_postagem = database.Column(database.DateTime, nullable=False, default=datetime.now)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)