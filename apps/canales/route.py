from flask import Blueprint
from apps.canales.controller import ServidorController

app_canal= Blueprint('canal', __name__)

app_canal.route('/crear_servidor',methods=['POST'])(ServidorController.create_servidor)
app_canal.route('/servidores',methods=['GET'])(ServidorController.get_servidores_publicos)
app_canal.route('/servidores_all',methods=['GET'])(ServidorController.get_all_servidores)
app_canal.route('/editar_servidor/<token>',methods=['PUT'])(ServidorController.update_servidor)
#app_servidor.route('/crear_servidor',methods=['POST'])(ServidorController.create_servidor)
#app_servidor.route('/crear_servidor',methods=['POST'])(ServidorController.create_servidor)