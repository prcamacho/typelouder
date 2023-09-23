from flask import Blueprint
from api.controllers.imagen_controller import ImagenController

app_media= Blueprint('media', __name__, url_prefix='/media')

app_media.route('/servidores/<filename>',methods=['GET'])(ImagenController.imagen_media_servidor)
app_media.route('/users/<filename>',methods=['GET'])(ImagenController.imagen_media_user)