from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'd24f396f2a891195866947f4df0e1e96'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://database_1pzo_user:WTcPujrAKtB1AKJi21rGfaPkUTaWTqHl@dpg-cig4aglph6erq6jc8e20-a/database_1pzo'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message='Faça Login Ou Cadastre-se Para Acessar'
login_manager.login_message_category='alert alert-danger'


from ProjectBlogJeff import routes

