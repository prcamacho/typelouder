from flask import request, jsonify
from flask_login import current_user
from api.models.mensaje_model import Mensaje, Reaccion
from api.models.canal_model import Canal
from werkzeug.security import generate_password_hash, check_password_hash

class MensajeController:
    @classmethod
    def create_mensaje(cls, id_canal):
        mensaje= request.form['mensaje']
        id_usuario= current_user.id
        if mensaje:
            msj= Mensaje(id_usuario=id_usuario, id_canal=id_canal, mensaje=mensaje)    
            Mensaje.create_mensaje(msj)
            return jsonify({'message':'Mensaje creado con exito'}, 200)
    
    @classmethod
    def get_mensaje(cls, id):
        mensaje= Mensaje.get_mensaje(Mensaje(id=id))
        if mensaje:
            return jsonify(mensaje.serialize(), 200)
        return jsonify({'message':'No se ha encontrado mensaje'}, 400)
    
    @classmethod
    def get_mensajes_canal(cls, id_canal):
        mensajes= Mensaje.get_mensaje_canal(Canal(id=id_canal))
        lista=[]
        if mensajes is not None:
            mensajes.reverse()
            for mensaje in mensajes:
                lista.append(mensaje.serialize())
            return jsonify(lista, 200)
        return jsonify({'message':'No hay mensajes'},404)
    
    @classmethod
    def get_all_mensajes(cls):
        mensajes= Mensaje.get_mensajes()
        lista=[]
        for mensaje in mensajes:
            lista.append(mensaje.serialize())
        return jsonify(lista, 200)
    
    @classmethod
    def update_mensaje(cls, id):
        mensaje= request.form['mensaje']
        id_usuario= current_user.id
        msj= Mensaje(id=id, id_usuario=id_usuario, mensaje=mensaje)    
        Mensaje.update_mensaje(msj)
        return jsonify({'message':'Mensaje editado con exito'}, 200)
    
    @classmethod
    def delete_mensaje(cls, id):
        mensaje= Mensaje.get_mensaje(Mensaje(id=id))
        mensaje.id_usuario= current_user.id
        if mensaje and mensaje.id_usuario == current_user.id:
            Mensaje.delete_mensaje(mensaje)
            return jsonify({'message':'Mensaje eliminado'}, 200)
        return jsonify({'message':'No es posible eliminar el mensaje'})
    
    @classmethod
    def reaccionar(cls, id_mensaje):
        id_usuario=current_user.id
        reaccion= 'true'== request.form['raccion']
        mensaje=Mensaje(id=id_mensaje, id_usuario=id_usuario)
        Reaccion.reaccionar(Reaccion(reaccion=reaccion),mensaje)
        return jsonify({'message':'Que reaccionas gil!!??'})
    
    @classmethod
    def update_reaccion(cls,id):
        reaccion= None
        if reaccion != None:
            reaccion= 'true'== request.form['raccion']
        Reaccion.update_reaccion(Reaccion(id=id, reaccion=reaccion))
        return jsonify({'message':'Decidite, vas a estar deacuerdo o no?'})    
            