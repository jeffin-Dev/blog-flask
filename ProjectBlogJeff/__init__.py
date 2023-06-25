from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'd24f396f2a891195866947f4df0e1e96'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

database = SQLAlchemy(app)

from ProjectBlogJeff import routes

