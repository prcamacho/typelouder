from flask import Flask, render_template
from api.users.routes import app_usuario
from api.servidores.route import app_servidor
from api.mensajes.route import app_mensaje
from api.canales.route import app_canal
from config import Config
from flask_login import login_required
from flask_cors import CORS
    
typelouder = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
CORS(typelouder, supports_credentials=True)

typelouder.secret_key = Config.SECRET_KEY

typelouder.config['TEMPLATES_AUTO_RELOAD'] = True

typelouder.config['MAIL_SERVER'] = Config.CREDENCIALES_EMAIL['email_host']
typelouder.config['MAIL_PORT'] = Config.CREDENCIALES_EMAIL['email_port']
typelouder.config['MAIL_USE_TLS'] = Config.CREDENCIALES_EMAIL['email_use_tls']
typelouder.config['MAIL_USERNAME'] = Config.CREDENCIALES_EMAIL['email_host_user']
typelouder.config['MAIL_PASSWORD'] = Config.CREDENCIALES_EMAIL['email_host_password']
typelouder.register_blueprint(app_usuario)
typelouder.register_blueprint(app_servidor)
typelouder.register_blueprint(app_mensaje)
typelouder.register_blueprint(app_canal)

@typelouder.route('/')
@login_required
def home():
    return render_template('home/index.html')

    



