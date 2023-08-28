from flask import request, jsonify
from flask_login import current_user
from apps.mensajes.model import Mensaje
from apps.canales.model import Canal
from werkzeug.security import generate_password_hash, check_password_hash
from apps.servidores.model import Servidor

class CanalController:
    @classmethod
    def create_canal(cls, token_servidor):
        nombre= request.form['nombre']
        servidor= Servidor.get_servidor(Servidor(token=token_servidor))
        Canal.create_canal(Canal(nombre=nombre, id_servidor=servidor.id))
        return jsonify({'message':'Mensaje creado con exito'}, 200)
    
    @classmethod
    def get_canal(cls, id):
        canal= Canal.get_canal(Canal(id=id))
        dic= {
            'id':canal.id,
            'nombre':canal.nombre,
            'id_servidor':canal.id_servidor,
            'fecha_creacion':canal.fecha_creacion
        }
        return jsonify(dic, 200)
    
    @classmethod
    def get_canales_servidor(cls, token_servidor):
        servidor= Servidor.get_servidor(Servidor(token=token_servidor))
        canales= Canal.get_canal_servidor(Canal(id_servidor=servidor.id))
        lista=[]
        for canal in canales:
            dic= {
                'id':canal.id,
                'nombre':canal.nombre,
                'id_servidor':canal.id_servidor,
                'fecha_creacion':canal.fecha_creacion
            }
            lista.append(dic)
        return jsonify(lista, 200)
    
    @classmethod
    def get_all_canales(cls):
        canales= Canal.get_canales()
        lista=[]
        for canal in canales:
            dic= {
                'id':canal.id,
                'nombre':canal.nombre,
                'id_servidor':canal.id_servidor,
                'fecha_creacion':canal.fecha_creacion
            }
            lista.append(dic)
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