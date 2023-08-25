from flask_mail import Mail
from flask_login import LoginManager, UserMixin
from .database import DatabaseConnection as conn
from .users.models import User

MAIL= Mail()

login_manager= LoginManager()
        
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