from flask import request, jsonify
from flask_login import current_user
from api.models.mensaje_model import Mensaje
from api.models.canal_model import Canal
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.servidor_model import Servidor
from api.models.exceptions import NotFound, InvalidDataError

class CanalController:
    @classmethod
    def create_canal(cls, token_servidor):
        nombre= request.form['nombre']
        if len(nombre) < 3 or len(nombre) > 10:
            raise InvalidDataError("Nombre del canal inválido",
                                   "El nombre del canal debe tener entre 3 y 10 caracteres")
        servidor= Servidor.get_servidor(Servidor(token=token_servidor))
        Canal.create_canal(Canal(nombre=nombre, id_servidor=servidor.id))
        return jsonify({'message':'Canal creado con exito'}, 200)
    
    @classmethod
    def get_canal(cls, id):
        canal= Canal.get_canal(Canal(id=id))
        if canal:
            dic= canal.serialize()
            return jsonify(dic, 200)
        raise NotFound("canal no encontrado", "No se encontro el canal")
    
    @classmethod
    def get_canales_servidor(cls, token_servidor):
        servidor= Servidor.get_servidor(Servidor(token=token_servidor))
        canales= Canal.get_canal_servidor(Canal(id_servidor=servidor.id))
        lista=[]
        if canales:
            for canal in canales:
                lista.append(canal.serialize())
            return jsonify(lista, 200)
        else:
            raise NotFound("No se encontraron canales", "No se encontraron canales en el servidor")
    
    @classmethod
    def get_all_canales(cls):
        canales= Canal.get_canales()
        lista=[]
        for canal in canales:
            lista.append(canal.serialize())
        return jsonify(lista, 200)
    
    @classmethod
    def update_canal(cls, id):
        nombre= request.form['nombre']
        Canal.update_canal(Canal(id=id, nombre=nombre))
        return jsonify({'message':'Canal editado con exito'}, 200)
    
    @classmethod
    def delete_canal(cls, id):
        CanalController.delete_canal(Canal(id=id))
        return jsonify({'message':'Canal eliminado'})