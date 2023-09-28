from api import typelouder
from api.database import DatabaseConnection
from config import Config
from api.extensiones import MAIL, login_manager, rutas_media
#from api.events import socketio

#inicia la aplicacion
if __name__ == '__main__':
    DatabaseConnection.create_tables()
    MAIL.init_app(typelouder)
    login_manager.init_app(typelouder)
    #socketio.init_app(typelouder)
    rutas_media()  
    typelouder.run(debug=Config.DEBUG, port=Config.PORT)