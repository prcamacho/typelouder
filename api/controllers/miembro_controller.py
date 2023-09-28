from flask_login import current_user
from api.models.miembo_model import Miembro
from flask import jsonify
from api.models.servidor_model import Servidor

class MiembroController:
    @classmethod
    def unirse_servidor(cls, token_servidor):
        servidor = Servidor.get_servidor(Servidor(token = token_servidor))
        if servidor:
            miembro= Miembro(id_usuario=current_user.id, id_servidor=servidor.id)
            Miembro.unirse_servidor(miembro)
            return jsonify({'message':'Miembro registrado'} , 200)
        return jsonify({'message':'Error al unirse al sevidor'}, 400)
    
    @classmethod
    def salir_servidor(cls, token_servidor):
        servidor = Servidor.get_servidor(Servidor(token = token_servidor))
        if servidor:
            miembro= Miembro(id_usuario=current_user.id, id_servidor=servidor.id)
            Miembro.salir_servidor(miembro)
            return jsonify({'message':'Ha salido del servidor'} , 200)
        return jsonify({'message':'Error al salirse del sevidor'}, 400)
    
    @classmethod
    def es_miembro(cls, token_servidor):
        servidor = Servidor.get_servidor(Servidor(token = token_servidor))
        if servidor:
            miembro= Miembro(id_usuario=current_user.id, id_servidor=servidor.id)
            es_miembro= Miembro.es_miembro(miembro)
            if es_miembro:
                return jsonify(es_miembro,200)
            return jsonify(es_miembro,200)
        return jsonify({'message':'No se encontro servidor'},404)