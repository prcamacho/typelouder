from flask import Blueprint
from api.controllers.mensaje_controller import MensajeController

app_mensaje= Blueprint('mensaje', __name__, url_prefix='/mensajes')

app_mensaje.route('/crear',methods=['POST'])(MensajeController.create_mensaje)
app_mensaje.route('/<int:id>',methods=['GET'])(MensajeController.get_mensaje)
app_mensaje.route('/<canal>',methods=['GET'])(MensajeController.get_mensajes_canal)
app_mensaje.route('/all',methods=['GET'])(MensajeController.get_all_mensajes)
app_mensaje.route('/editar',methods=['PUT'])(MensajeController.update_mensaje)
app_mensaje.route('/eliminar/<int:id>',methods=['DELETE'])(MensajeController.delete_mensaje)
app_mensaje.route('/reaccionar/<int:id_mensaje>',methods=['POST'])(MensajeController.reaccionar)
app_mensaje.route('/editar_reaccion/<int:id>', methods=['PUT'])(MensajeController.update_reaccion)