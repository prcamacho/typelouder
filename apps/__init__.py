from flask import Flask
from .users import app_usuario
from config import Config

typelouder= Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

typelouder.register_blueprint(app_usuario)

typelouder.config.from_object(Config)

