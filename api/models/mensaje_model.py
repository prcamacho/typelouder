from api.database import DatabaseConnection as conn
from api.models.user_model import User
from api.models.canal_model import Canal
from datetime import datetime

class Mensaje:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.id_usuario = kwargs.get('id_usuario')
        self.id_canal = kwargs.get('id_canal')
        self.mensaje = kwargs.get('mensaje')
        self.fecha_mensaje = kwargs.get('fecha_mensaje')
    
    def serialize(self):
        return {
            'id':self.id,
            'usuario':User.get_user(User(id=self.id_usuario)).serialize_basico(),
            'canal':Canal.get_canal(Canal(id=self.id_canal)).serialize(),
            'mensaje':self.mensaje,
            'fecha_mensaje':self.fecha_mensaje.strftime("%d/%m/%y %H:%M")
        }
    
    @classmethod
    def create_mensaje(cls, mensaje):
        query='''INSERT INTO mensajes(id_usuario, id_canal, mensaje)
                VALUES(%s,%s,%s)'''
        params=(mensaje.id_usuario, mensaje.id_canal, mensaje.mensaje,)
        conn.execute_query(query,params)
        
    @classmethod    
    def get_mensaje(cls, mensaje):
        query='''SELECT * FROM mensajes WHERE id=%s'''
        params=(mensaje.id,)
        result=conn.fetch_one(query,params)
        if result is not None:
            return Mensaje(id=result[0], id_usuario=result[1], id_canal=result[2], mensaje=result[3], fecha_mensaje=result[4])
        return None   
    
    @classmethod    
    def get_mensaje_canal(cls, canal):
        query='''SELECT * FROM mensajes WHERE id_canal=%s'''
        params=(canal.id,)
        results=conn.fetch_all(query,params)
        if results:
            lista_servidores=[]
            for result in results:
                lista_servidores.append(Mensaje(id=result[0], id_usuario=result[2], id_canal=result[1], mensaje=result[3], fecha_mensaje=result[4]))
            return lista_servidores  
        return None  
    
    @classmethod
    def get_mensajes(cls):
        query='''SELECT * FROM mensajes'''
        results=conn.fetch_all(query)
        if results is not None:
            lista_servidores=[]
            for result in results:
                lista_servidores.append(Mensaje(id=result[0], id_usuario=result[2], id_canal=result[1], mensaje=result[3], fecha_mensaje=result[4]))
            return lista_servidores    
        return None   
    
    @classmethod
    def update_mensaje(cls,mensaje):
        query='''UPDATE mensajes SET mensaje=%s WHERE id=%s'''
        params=(mensaje.mensaje,mensaje.id)
        conn.execute_query(query,params)
    
    @classmethod
    def delete_mensaje(cls,mensaje):
        query='''DELETE FROM mensajes WHERE id=%s AND id_usuario=%s'''
        params= (mensaje.id, mensaje.id_usuario,)
        conn.execute_query(query, params)
        
        
class Reaccion:
    def __init__(self, id=None, id_menasje=None, id_usuario=None, reaccion=None):
        self.id= id
        self.id_mensaje= id_menasje
        self.id_usuario= id_usuario
        self.reaccion= reaccion
    
    @classmethod    
    def reaccionar(cls, reaccion, mensaje):
        query= '''INSERT INTO reacciones (reaccion, id_mensaje, id_usuario) 
                VALUES (%s,%s,%s)'''
        params= (reaccion.reaccion, mensaje.id, mensaje.id_usuario,)
        conn.execute_query(query,params)                   
        
    @classmethod
    def update_reaccion(cls, reaccion):
        query= '''UPDATE reacciones SET reaccion= %s WHERE id=%s'''
        params= (reaccion.reaccion, reaccion.id,)
        conn.execute_query(query,params)