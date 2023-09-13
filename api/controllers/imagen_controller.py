from api.models.imagen_model import Imagen
from flask import send_from_directory
from config import Config

class ImagenController:
    
    @classmethod
    def imagen_media(cls,filename):
        return send_from_directory('../'+Config.MEDIA_SERVIDOR,filename)