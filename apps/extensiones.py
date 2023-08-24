from flask_mail import Mail
from flask_login import LoginManager, UserMixin
from .conector import DatabaseConnection as conn

MAIL= Mail()

login_manager= LoginManager()

class User(UserMixin):
    def __init__(self, user_id,username,nombre,apellido,email):
        self.id=user_id
        self.username=username
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        
@login_manager.user_loader
def load_user(user_id):
    '''crea el usuario apto para el login'''
    query="SELECT * FROM usuarios WHERE id = %s"
    usuario = conn.fetch_one(query,(user_id,))
    conn.close_connection()
    if usuario:
        user = User(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4])
        return user
    return None        