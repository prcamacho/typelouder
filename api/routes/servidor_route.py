from flask import Blueprint
from api.controllers.servidor_controller import ServidorController

app_servidor= Blueprint('servidor', __name__, url_prefix='/servidores')

app_servidor.route('/crear_servidor',methods=['POST'])(ServidorController.create_servidor)
app_servidor.route('/',methods=['GET'])(ServidorController.get_servidores_publicos)
app_servidor.route('/all',methods=['GET'])(ServidorController.get_all_servidores)
app_servidor.route('/editar_servidor/<token>',methods=['PUT'])(ServidorController.update_servidor)
app_servidor.route('/eliminar_servidor/<token>',methods=['DELETE'])(ServidorController.delete_servidor)

