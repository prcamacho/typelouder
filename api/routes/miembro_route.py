from flask import Blueprint
from api.controllers.miembro_controller import MiembroController

app_miembro= Blueprint('miembro', __name__, url_prefix='/miembros')

app_miembro.route('/unirse/<int:id_servidor>', methods=['POST'])(MiembroController.unirse_servidor)
app_miembro.route('/salir/<int:id_servidor>', methods=['POST'])(MiembroController.salir_servidor)