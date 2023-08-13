from flask import Flask
from .users import app_usuario
from config import Config
from flask_mail import Mail
from flask_login import LoginManager
#registro de aplicaciones y configuracion

typelouder= Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

typelouder.register_blueprint(app_usuario)
typelouder.secret_key= Config.SECRET_KEY
login_manager=LoginManager(typelouder)
typelouder.config['MAIL_SERVER'] = Config.CREDENCIALES_EMAIL['email_host']
typelouder.config['MAIL_PORT'] = Config.CREDENCIALES_EMAIL['email_port']
typelouder.config['MAIL_USE_TLS'] = Config.CREDENCIALES_EMAIL['email_use_tls']
typelouder.config['MAIL_USERNAME'] = Config.CREDENCIALES_EMAIL['email_host_user']
typelouder.config['MAIL_PASSWORD'] = Config.CREDENCIALES_EMAIL['email_host_password']

mail= Mail(typelouder)

typelouder.config.from_object(Config)

