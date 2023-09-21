from flask_mail import Mail
from flask_login import LoginManager, UserMixin
from .database import DatabaseConnection as conn
from .models.user_model import User
from config import Config
import os

MAIL= Mail()

login_manager= LoginManager()
        
@login_manager.user_loader
def load_user(user_id):
    query="SELECT * FROM usuarios WHERE id = %s"
    usuario = conn.fetch_one(query,(user_id,))
    conn.close_connection()
    if usuario:
        user = User(id=usuario[0],username=usuario[1],nombre=usuario[2],apellido=usuario[3],email=usuario[4])
        return user
    return None        

def rutas_media():
    if not os.path.exists(Config.MEDIA_FOLDER):
        os.makedirs(Config.MEDIA_FOLDER)
    if not os.path.exists(Config.MEDIA_SERVIDOR):
        os.makedirs(Config.MEDIA_SERVIDOR)  
    if not os.path.exists(Config.MEDIA_USER):
        os.makedirs(Config.MEDIA_USER)      