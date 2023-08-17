from flask_mail import Mail
from flask_login import LoginManager, UserMixin
from .conector import DatabaseConnection as conn

MAIL= Mail()

login_manager= LoginManager()

class User(UserMixin):
    def __init__(self, user_id):
        self.id=user_id
        
@login_manager.user_loader
def load_user(user_id):
    query="SELECT * FROM usuarios WHERE id = %s"
    usuario = conn.fetch_one(query,(user_id,))
    conn.close_connection()
    if usuario:
        user = User(usuario[0])
        return user
    return None        