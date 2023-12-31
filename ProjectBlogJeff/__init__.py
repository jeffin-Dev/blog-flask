from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd24f396f2a891195866947f4df0e1e96'
print('oi')

if os.getenv("DATABASE_URL"):
    print('cheguei aq 1')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://database_6sxg_user:cXekSxIjegRYcximW1CcwXkcxAPaeH6i@dpg-cig5sf5ph6erq6jlp4q0-a.oregon-postgres.render.com/database_6sxg'
else:
    print('cheguei aq 2')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message='Faça Login Ou Cadastre-se Para Acessar'
login_manager.login_message_category='alert alert-danger'

from ProjectBlogJeff import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print ('data de base criada')
else:
    print ('data de base já existente')


from ProjectBlogJeff import routes

