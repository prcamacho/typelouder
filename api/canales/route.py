from flask import Blueprint
from api.canales.controller import CanalController

app_canal= Blueprint('canal', __name__)

app_canal.route('/crear_canal',methods=['POST'])(CanalController.create_canal)
app_canal.route('/canales/<token_servidor>',methods=['GET'])(CanalController.get_canales_servidor)
app_canal.route('/canales_all',methods=['GET'])(CanalController.get_all_canales)
app_canal.route('/editar_canal/<int:id>',methods=['PUT'])(CanalController.update_canal)
app_canal.route('/eliminar_canal/<int:id>',methods=['DELETE'])(CanalController.delete_canal)
