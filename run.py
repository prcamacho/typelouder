from apps import typelouder
from apps.conector import DatabaseConnection
from config import Config
from apps.extensiones import MAIL, login_manager


#inicia la aplicacion
if __name__ == '__main__':
    DatabaseConnection.create_tables()
    MAIL.init_app(typelouder)
    login_manager.init_app(typelouder)
    typelouder.run(debug=Config.DEBUG, port=Config.PORT)