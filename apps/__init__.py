from flask import Flask, render_template
from .users import app_usuario
from config import Config
    
typelouder = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

typelouder.secret_key = Config.SECRET_KEY

typelouder.config['TEMPLATES_AUTO_RELOAD'] = True

typelouder.config['MAIL_SERVER'] = Config.CREDENCIALES_EMAIL['email_host']
typelouder.config['MAIL_PORT'] = Config.CREDENCIALES_EMAIL['email_port']
typelouder.config['MAIL_USE_TLS'] = Config.CREDENCIALES_EMAIL['email_use_tls']
typelouder.config['MAIL_USERNAME'] = Config.CREDENCIALES_EMAIL['email_host_user']
typelouder.config['MAIL_PASSWORD'] = Config.CREDENCIALES_EMAIL['email_host_password']
typelouder.register_blueprint(app_usuario)

@typelouder.route('/')
def home():
    return render_template('home/index.html')

    



