from api import typelouder
from api.database import DatabaseConnection
from config import Config
from api.extensiones import MAIL, login_manager
from api.database import cargar_datos

#inicia la aplicacion
if __name__ == '__main__':
    DatabaseConnection.create_tables()
    MAIL.init_app(typelouder)
    login_manager.init_app(typelouder)
    # try:
    #     cargar_datos()
    # except:
    #     pass    
    typelouder.run(debug=Config.DEBUG, port=Config.PORT)