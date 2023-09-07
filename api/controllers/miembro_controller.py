from flask_login import current_user
from api.models.miembo_model import Miembro
from flask import jsonify

class MiembroController:
    @classmethod
    def unirse_servidor(cls, id_servidor):
        miembro= Miembro(id_usuario=current_user.id, id_servidor=id_servidor)
        Miembro.unirse_servidor(miembro)
        return jsonify({'message':'Miembro registrado'} , 200)
    
    @classmethod
    def salir_servidor(cls, id_servidor):
        miembro= Miembro(id_usuario=current_user.id, id_servidor=id_servidor)
        Miembro.salir_servidor(miembro)
        return jsonify({'message':'Ha salido del servidor'} , 200)