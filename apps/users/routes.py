from flask import Blueprint
from .controller import UserController

app_usuario= Blueprint('user', __name__) 

app_usuario.route('/registro', methods=['POST'])(UserController.create_user)
app_usuario.route('/confirmar_email/<token>', methods=['GET'])(UserController.confirmar_email)
app_usuario.route('/login', methods=['POST'])(UserController.login)
app_usuario.route('/logout', methods=['GET'])(UserController.logout)
app_usuario.route('/password_reset', methods=['POST'])(UserController.password_reset)
app_usuario.route('/nuevo_password/<token>', methods=['PUT'])(UserController.nuevo_password)
app_usuario.route('/editar_usuario', methods=['PUT'])(UserController.edit_user)
app_usuario.route('/editar_password',methods=['PUT'])(UserController.edit_password)
app_usuario.route('/usuarios/<int:id>',methods=['GET'])(UserController.usuario)
app_usuario.route('/usuarios',methods=['GET'])(UserController.lista_usuarios)
