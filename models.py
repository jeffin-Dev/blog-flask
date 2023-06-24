from main import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(10), nullable=False, unique=True)
    email = database.Column(database.String, unique=True, nullabla=False)
    senha = database.Column(database.String, nullable=False)
    foto_de_perfil = database.Column(database.String, default='default.jpg')


class Post(database.Model) :
    id= database.Column(database.Integer,primary_key=True)
    tituto= database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_de_postagem = database.Co0lumn(database.DateTime, nullable=False default=datetime.now)

