from api.models.imagen_model import Imagen
from flask import send_from_directory
from config import Config

class ImagenController:
    
    @classmethod
    def imagen_media_servidor(cls,filename):
        return send_from_directory('../'+Config.MEDIA_SERVIDOR,filename)
    
    @classmethod
    def imagen_media_user(cls,filename):
        return send_from_directory('../'+Config.MEDIA_USER,filename)