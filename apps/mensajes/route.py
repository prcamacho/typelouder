from flask import Blueprint
from apps.mensajes.controller import MensajeController

app_mensaje= Blueprint('mensaje', __name__)

app_mensaje.route('/crear_mensaje',methods=['POST'])(MensajeController.create_mensaje)
app_mensaje.route('/mensajes/<int:id>',methods=['GET'])(MensajeController.get_mensaje)
app_mensaje.route('/mensajes/<canal>',methods=['GET'])(MensajeController.get_mensajes_canal)
app_mensaje.route('/mensajes_all',methods=['GET'])(MensajeController.get_all_mensajes)
app_mensaje.route('/editar_mensaje',methods=['PUT'])(MensajeController.update_mensaje)
app_mensaje.route('/eliminar_mensaje/<int:id>',methods=['DELETE'])(MensajeController.delete_mensaje)

app_mensaje.route('/reaccionar/<int:id_mensaje>',methods=['POST'])(MensajeController.reaccionar)
app_mensaje.route('/editar_reaccion/<int:id>', methods=['PUT'])(MensajeController.update_reaccion)