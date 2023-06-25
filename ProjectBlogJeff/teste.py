from ProjectBlogJeff.models import Usuario
from ProjectBlogJeff import app, database

with app.app_context():
    usuarios = Usuario.query.first()
    print(usuarios.email)