from flask import request, jsonify, url_for
import uuid
from flask_login import current_user
from api.models.servidor_model import Servidor
from api.models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.imagen_model import Imagen
from config import Config
from flask import send_from_directory
from api.routes.imagen_route import app_media
from api.controllers.miembro_controller import MiembroController
from api.models.canal_model import Canal
import math

class ServidorController:
    @classmethod
    def create_servidor(cls):
        nombre= request.form['nombre']
        descripcion= request.form['descripcion']
        imagen= request.files['imagen']
        privado= 'true'== request.form['privado']
        password= None
        id_categoria= request.form['id_categoria']
        id_usuario_creador= current_user.id
        token=str(uuid.uuid4())  
        filename = Imagen.guardar_imagen(imagen,request,Config.MEDIA_SERVIDOR,(250,250))
        if privado:
            password= generate_password_hash(request.form['password'])
        servidor= Servidor(nombre=nombre, descripcion=descripcion,imagen=filename,privado=privado,
                                password=password,token=token,id_usuario_creador=id_usuario_creador,id_categoria=id_categoria )    
        Servidor.create_servidor(servidor)
        serv_creado = Servidor.get_servidor(Servidor(token=token))
        MiembroController.unirse_servidor(token)
        Canal.create_canal(Canal(nombre='General',id_servidor=serv_creado.id))
        return jsonify({'message':'Servidor creado con exito'}, 200)
    
    @classmethod
    def get_servidores_publicos(cls):
        servidores= Servidor.get_servidores()
        lista=[]
        for servidor in servidores:
            if not servidor.privado:
                servidor_data= servidor.serialize()
                servidor_data['imagen']= send_from_directory('media/servicios',servidor_data['imagen'])
                lista.append(servidor_data)
        return jsonify(lista, 200)
    
    @classmethod
    def get_servidores_user(cls):
        servidores= Servidor.get_servidores_user(User(id=current_user.id))
        print(servidores)
        if servidores:
            lista=[]
            for servidor in servidores:
                servidor_data= servidor.serialize()
                lista.append(servidor_data)
            return jsonify(lista,200)
        return jsonify({'message':'No hay servidores'}, 404)
    
    @classmethod
    def get_all_servidores(cls):
        pagina = int(request.args.get('pagina', 1))
        elementos_pagina = 11
        inicio = (pagina - 1) * elementos_pagina
        fin = inicio + elementos_pagina
        servidores= Servidor.get_servidores()
        lista=[]
        if servidores is not None:
            for servidor in servidores:
                lista.append([servidor[0].serialize(),servidor[1]]) 
            return jsonify(lista[inicio:fin],math.ceil(len(lista)/elementos_pagina), 200)
        return jsonify({'message':'No hay servidores'})
    
    @classmethod
    def get_servidores_like(cls):
        nombre_servidor = request.args.get('q', '')
        print(nombre_servidor)
        servidores = Servidor.get_servidores_like(nombre_servidor)
        lista=[]
        if servidores is not None:
            for servidor in servidores:
                lista.append([servidor[0].serialize(),servidor[1]])
            return jsonify(lista, 200)
        return jsonify({'message':'No hay servidores'})
        
    
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
        servidor= Servidor.get_servidor(Servidor(token=token))
        imagen_servidor= servidor.imagen
        if imagen_servidor:
            Imagen.delete_image(Config.MEDIA_SERVIDOR, imagen_servidor)
        Servidor.delete_servidor(Servidor(id_usuario_creador=id_usuario_creador, token=token))
        return jsonify({'message':'Servidor eliminado'})         