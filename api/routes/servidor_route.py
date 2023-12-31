from flask import Blueprint
from api.controllers.servidor_controller import ServidorController

app_servidor= Blueprint('servidor', __name__, url_prefix='/servidores')
ALLOWED_EXTENSION = set(['png','jpg','jpeg'])

app_servidor.route('/crear',methods=['POST'])(ServidorController.create_servidor)
app_servidor.route('/',methods=['GET'])(ServidorController.get_servidores_user)
app_servidor.route('/all',methods=['GET'])(ServidorController.get_all_servidores)
app_servidor.route('/editar/<token>',methods=['PUT'])(ServidorController.update_servidor)
app_servidor.route('/eliminar/<token>',methods=['DELETE'])(ServidorController.delete_servidor)
app_servidor.route('/like',methods=['GET'])(ServidorController.get_servidores_like)
app_servidor.route('/categoria/<int:id_categoria>',methods=['GET'])(ServidorController.get_servidores_categorias)

