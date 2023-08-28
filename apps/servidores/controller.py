from flask import request, jsonify
import uuid
from flask_login import current_user
from apps.servidores.model import Servidor
from werkzeug.security import generate_password_hash, check_password_hash

class ServidorController:
    @classmethod
    def create_servidor(cls):
        nombre= request.form['nombre']
        descripcion= request.form['descripcion']
        imagen= request.form['imagen']
        privado= 'true'== request.form['privado']
        password= None
        id_categoria= request.form['id_categoria']
        #id_usuario_creador= current_user.id
        id_usuario_creador= 1
        token=str(uuid.uuid4())
        if privado:
            password= generate_password_hash(request.form['password'])
        servidor= Servidor(nombre=nombre, descripcion=descripcion,imagen=imagen,privado=privado,
                                password=password,token=token,id_usuario_creador=id_usuario_creador,id_categoria=id_categoria )    
        Servidor.create_servidor(servidor)
        return jsonify({'message':'Servidor creado con exito'}, 200)
    
    @classmethod
    def get_servidores_publicos(cls):
        servidores= Servidor.get_servidores()
        lista=[]
        for servidor in servidores:
            if not servidor.privado:
                dic= {
                    'id':servidor.id,
                    'nombre':servidor.nombre,
                    'descripcion':servidor.descripcion,
                    'imagen':servidor.imagen,
                    'fecha_creacion':servidor.fecha_creacion,
                    'privado':servidor.privado,
                    'token':servidor.token,
                    'id_usuario_creador':servidor.id_usuario_creador,
                    'id_categoria':servidor.id_categoria
                }
                lista.append(dic)
        return jsonify(lista, 200)
    
    @classmethod
    def get_all_servidores(cls):
        servidores= Servidor.get_servidores()
        lista=[]
        for servidor in servidores:
            dic= {
                'id':servidor.id,
                'nombre':servidor.nombre,
                'descripcion':servidor.descripcion,
                'imagen':servidor.imagen,
                'fecha_creacion':servidor.fecha_creacion,
                'privado':servidor.privado,
                'token':servidor.token,
                'id_usuario_creador':servidor.id_usuario_creador,
                'id_categoria':servidor.id_categoria
            }
            lista.append(dic)
        return jsonify(lista, 200)
    
    @classmethod
    def update_servidor(cls, token):
        nombre= request.form['nombre']
        descripcion= request.form['descripcion']
        imagen= request.form['imagen']
        privado= 'true'== request.form['privado']
        password= None
        #id_usuario_creador= current_user.id
        id_usuario_creador=1
        if privado:
            password= generate_password_hash(request.form['password'])
        servidor= Servidor(nombre=nombre, descripcion=descripcion,imagen=imagen,privado=privado,
                                password=password,token=token,id_usuario_creador=id_usuario_creador)    
        Servidor.update_servidor(servidor)
        return jsonify({'message':'Servidor editado con exito'}, 200)

    @classmethod
    def delete_servidor(cls, token):
        #id_usuario_creador=current_user.id 
        id_usuario_creador= 1
        Servidor.delete_servidor(Servidor(id_usuario_creador=id_usuario_creador, token=token))
        return jsonify({'message':'Servidor eliminado'})
            