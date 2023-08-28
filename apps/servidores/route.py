from flask import Blueprint
from apps.servidores.controller import ServidorController

app_servidor= Blueprint('servidor', __name__)

app_servidor.route('/crear_servidor',methods=['POST'])(ServidorController.create_servidor)
app_servidor.route('/servidores',methods=['GET'])(ServidorController.get_servidores_publicos)
app_servidor.route('/servidores_all',methods=['GET'])(ServidorController.get_all_servidores)
app_servidor.route('/editar_servidor/<token>',methods=['PUT'])(ServidorController.update_servidor)
app_servidor.route('/eliminar_servidor/<token>',methods=['DELETE'])(ServidorController.delete_servidor)
#app_servidor.route('/crear_servidor',methods=['POST'])(ServidorController.create_servidor)

