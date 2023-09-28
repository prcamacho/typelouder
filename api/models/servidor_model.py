from api.database import DatabaseConnection as conn
from api.models.categoria_model import Categoria
from api.models.user_model import User
from flask import request, url_for
from api.models.exceptions import NotFound, InvalidDataError
import re


class Servidor:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')
        self.imagen = kwargs.get('imagen')
        self.fecha_creacion = kwargs.get('fecha_creacion')
        self.privado = kwargs.get('privado')
        self.password = kwargs.get('password')
        self.token = kwargs.get('token')
        self.id_usuario_creador = kwargs.get('id_usuario_creador')
        self.id_categoria = kwargs.get('id_categoria')
    
    def serialize(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'descripcion':self.descripcion,
            'imagen':str(request.url_root)+url_for(endpoint='media.imagen_media_servidor', filename= self.imagen),
            'fecha_creacion':self.fecha_creacion,
            'privado':self.privado,
            'token':self.token,
            'usuario_creador':User.get_user(User(id=self.id_usuario_creador)).serialize_basico(),
            'categoria':Categoria.get_categoria(Categoria(id=self.id_categoria)).serialize()
        }
    
    def serialize_basico(self):
        return {
            'id':self.id,
            'nombre':self.nombre
        }    
    
    @classmethod
    def create_servidor(cls, servidor):
        if None in [servidor.nombre, servidor.descripcion]:
            raise InvalidDataError("Datos faltantes", "Debe completar todos los campos")

            # Si el servidor es privado, verificar que se proporcione la contraseña
        if servidor.privado:
            if servidor.password is None:
                raise InvalidDataError("Contraseña faltante", "El servidor es privado y se requiere una contraseña")

            # Verificar si la contraseña cumple con los criterios
            if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', servidor.password):
                raise InvalidDataError("Contraseña inválida",
                                       "La contraseña debe tener al menos 8 caracteres, un número y un carácter especial")

        query='''INSERT INTO servidores(nombre, descripcion, imagen, 
                privado, password, token, id_usuario_creador, id_categoria)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
        params=(servidor.nombre, servidor.descripcion, servidor.imagen,
                servidor.privado, servidor.password, servidor.token, 
                servidor.id_usuario_creador, servidor.id_categoria)
        conn.execute_query(query,params)
    
    @classmethod    
    def get_servidor_id(cls, servidor):
        query='''SELECT * FROM servidores WHERE id=%s'''
        params=(servidor.id,)
        result=conn.fetch_one(query,params)
        if result is not None:
            return Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                            imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                            token=result[7], id_usuario_creador=result[8], id_categoria=result[9])
        raise NotFound("Servidor no encontrado", "El servidor con el ID proporcionado no existe")
    
    @classmethod    
    def get_servidores_user(cls, user):
        query='''SELECT * FROM servidores A INNER JOIN miembros B ON B.id_servidor = A.id INNER JOIN usuarios C ON B.id_usuario = C.id WHERE C.id=%s'''
        params=(user.id,)
        results=conn.fetch_all(query,params)
        if results is not None and len(results) > 0:
            lista = []
            for result in results:
                lista.append(Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                                      imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                                      token=result[7], id_usuario_creador=result[8], id_categoria=result[9]))
            return lista
        else:
            raise NotFound("No se encontraron servidores para el usuario", "El usuario no está unido a ningún servidor")
        
    @classmethod    
    def get_servidor(cls, servidor):
        query='''SELECT * FROM servidores WHERE token=%s'''
        params=(servidor.token,)
        result=conn.fetch_one(query,params)
        if result is not None:
            return Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                            imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                            token=result[7], id_usuario_creador=result[8], id_categoria=result[9])
        raise NotFound("Servidor no encontrado", "El servidor no existe")
    
    @classmethod
    def get_servidores_like(cls, nombre_servidor):
        query= """SELECT A.id, A.nombre, A.descripcion, A.imagen, A.fecha_creacion, A.privado, 
                A.password, A.token, A.id_usuario_creador, A.id_categoria, COALESCE(COUNT(B.id_usuario), 0) AS usuarios_servidor
                FROM typelouder.servidores A 
                LEFT JOIN typelouder.miembros B ON A.id = B.id_servidor
                WHERE nombre LIKE %s
                GROUP BY A.id, A.nombre, A.descripcion, A.imagen, A.fecha_creacion, A.privado, 
                A.password, A.token, A.id_usuario_creador, A.id_categoria;"""
        params= (f"%{nombre_servidor}%",)
        results= conn.fetch_all(query, params)
        if results is not None:
            lista_servidores=[]
            for result in results:
                lista_servidores.append([Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                            imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                            token=result[7], id_usuario_creador=result[8], id_categoria=result[9]),result[10]])
            return lista_servidores    
        return None   
        
    @classmethod
    def get_servidores(cls):
        # query='''SELECT * FROM servidores'''
        # results = conn.fetch_all(query)
        # if results is not None:
        #     lista_servidores=[]
        #     for result in results:
        #         lista_servidores.append(Servidor(id=result[0], nombre=result[1], descripcion=result[2],
        #                     imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
        #                     token=result[7], id_usuario_creador=result[8], id_categoria=result[9]))
        #     return lista_servidores    
        # return None  
        query='''SELECT A.id, A.nombre, A.descripcion, A.imagen, A.fecha_creacion, A.privado, 
                A.password, A.token, A.id_usuario_creador, A.id_categoria, COALESCE(COUNT(B.id_usuario), 0) AS usuarios_servidor
                FROM typelouder.servidores A 
                LEFT JOIN typelouder.miembros B ON A.id = B.id_servidor
                GROUP BY A.id, A.nombre, A.descripcion, A.imagen, A.fecha_creacion, A.privado, 
                A.password, A.token, A.id_usuario_creador, A.id_categoria;'''
        results = conn.fetch_all(query)
        if results is not None:
            lista_servidores=[]
            for result in results:
                lista_servidores.append([Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                            imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                            token=result[7], id_usuario_creador=result[8], id_categoria=result[9]),result[10]])
            return lista_servidores
        else:
            raise NotFound("No se encontraron servidores", "Todavía no se han creado servidores")
    
    @classmethod
    def update_servidor(cls,servidor):
        query='''UPDATE servidores SET nombre=%s, descripcion=%s, imagen=%s, privado=%s, password=%s
        WHERE token=%s and id_usuario_creador=%s'''
        params=(servidor.nombre, servidor.descripcion, servidor.imagen, servidor.privado,
                servidor.password, servidor.token, servidor.id_usuario_creador,)
        conn.execute_query(query,params)
    
    @classmethod
    def delete_servidor(cls,servidor):
        query= '''DELETE FROM servidores WHERE token=%s AND id_usuario_creador=%s'''
        params= (servidor.token, servidor.id_usuario_creador,)
        conn.execute_query(query,params)
        







    