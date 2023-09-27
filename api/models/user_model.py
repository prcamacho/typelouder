from flask_login import UserMixin
from api.database import DatabaseConnection as conn
from api.models.insignia_model import Insignia
from flask import request, url_for

class User(UserMixin):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.username = kwargs.get('username')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
        self.imagen = kwargs.get('imagen')
        self.activo = kwargs.get('activo')
        self.token = kwargs.get('token')
        self.id_insignia = kwargs.get('id_insignia')
    
    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'email':self.email,
            'fecha_nacimiento':self.fecha_nacimiento,
            'imagen':str(request.url_root)+url_for(endpoint='media.imagen_media_user', filename= self.imagen),
            'activo':self.activo,
            'insignia': Insignia.get_insignia(Insignia(id=self.id_insignia)).serialize()
        }
    
    def serialize_basico(self):
        return {
            'id':self.id,
            'username':self.username,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'imagen':str(request.url_root)+url_for(endpoint='media.imagen_media_user', filename= self.imagen),
        }    
    
    @classmethod    
    def create_user(cls, user):
        query='''INSERT INTO usuarios (username, nombre, apellido,email,password,fecha_nacimiento,token) 
        values (%s,%s,%s,%s,%s,%s,%s)'''
        params= (user.username,user.nombre,user.apellido,user.email,user.password,user.fecha_nacimiento,str(user.token),)
        conn.execute_query(query,params)
        
    @classmethod
    def get_user(cls, user):
        query= '''SELECT * FROM usuarios WHERE id = %s'''
        params = (user.id,)
        result = conn.fetch_one(query, params) 
        if result is not None:
            return User(
                id = result[0], 
                username = result[1], 
                nombre = result[2], 
                apellido = result[3],
                email = result[4],
                password= result[5],
                fecha_nacimiento = result[6],
                imagen = result[7], 
                activo = result[8],
                id_insignia = result[10]
                )
        return None    
    
    @classmethod
    def get_user_email(cls, user):
        query= '''SELECT * FROM usuarios WHERE email = %s'''
        params = (user.email,)
        result = conn.fetch_one(query, params) 
        if result is not None:
            return User(
                id = result[0], 
                username = result[1], 
                nombre = result[2], 
                apellido = result[3],
                email = result[4],
                password= result[5],
                fecha_nacimiento = result[6],
                imagen = result[7], 
                activo = result[8],
                id_insignia = result[10]
                )
        return None 
    
    @classmethod
    def get_users(cls):
        query= '''SELECT * FROM usuarios'''
        results = conn.fetch_all(query) 
        if results is not None:
            user_list=[]
            for result in results:
                user_list.append(User(id = result[0], 
                                    username = result[1], 
                                    nombre = result[2], 
                                    apellido = result[3],
                                    email = result[4],
                                    password= result[5],
                                    fecha_nacimiento = result[6],
                                    imagen = result[7], 
                                    activo = result[8],
                                    id_insignia = result[10]
                                      ))
            return user_list    
        return None 
        
    @classmethod
    def update_user(cls, user):
        query= '''UPDATE usuarios SET username=%s, nombre=%s, apellido=%s, imagen=%s WHERE id=%s'''
        params=(user.username,user.nombre,user.apellido,user.imagen,user.id,)
        conn.execute_query(query,params)   
    
    @classmethod
    def reset_user_pass(cls,user):
        query= '''UPDATE usuarios SET password=%s, token=null WHERE token=%s'''
        params= (user.password,user.token,)
        conn.execute_query(query,params)
        
    @classmethod    
    def edit_password(cls, user):
        query= '''UPDATE usuarios SET password=%s WHERE id=%s'''
        params= (user.password,user.id,)
        conn.execute_query(query,params)
    
    @classmethod
    def activate_user(cls, user):
        query= 'UPDATE usuarios set activo=1, token=null where token=%s'
        params=(user.token,)
        conn.execute_query(query,params)
        
    @classmethod
    def deactivate_user(cls, user):
        query= '''UPDATE usuarios set activo=0, token=%s WHERE id=%s'''
        params=(user.token,user.id,)
        conn.execute_query(query,params)