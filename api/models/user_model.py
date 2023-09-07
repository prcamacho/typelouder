from flask_login import UserMixin
from api.database import DatabaseConnection as conn
from api.models.insignia_model import Insignia

class User(UserMixin):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id',None)
        self.username = kwargs.get('username',None)
        self.nombre = kwargs.get('nombre',None)
        self.apellido = kwargs.get('apellido',None)
        self.email = kwargs.get('email',None)
        self.password = kwargs.get('password',None)
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento',None)
        self.activo = kwargs.get('activo',None)
        self.token = kwargs.get('token',None)
        self.id_insignia = kwargs.get('id_insignia',None)
    
    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'email':self.email,
            'fecha_nacimiento':self.fecha_nacimiento,
            'activo':self.activo,
            'insignia': Insignia.get_insignia(Insignia(id=self.id_insignia)).serialize()
        }
    
    def serialize_basico(self):
        return {
            'id':self.id,
            'username':self.username,
            'nombre':self.nombre,
            'apellido':self.apellido
        }    
    
    @classmethod    
    def create_user(cls, user):
        query='''INSERT INTO usuarios (username, nombre, apellido,email,password,fecha_nacimiento,token) 
        values (%s,%s,%s,%s,%s,%s,%s)'''
        params= (user.username,user.nombre,user.apellido,user.email,user.password,user.fecha_nacimiento,str(user.token),)
        conn.execute_query(query,params)
        conn.close_connection()
        
    @classmethod
    def get_user(cls, user):
        query= '''SELECT * FROM usuarios WHERE id = %s'''
        params = (user.id,)
        result = conn.fetch_one(query, params) 
        conn.close_connection()
        if result is not None:
            return User(
                id = result[0], 
                username = result[1], 
                nombre = result[2], 
                apellido = result[3],
                email = result[4],
                password= result[5],
                fecha_nacimiento = result[6],
                activo = result[7],
                id_insignia = result[9]
                )
        return None    
    
    @classmethod
    def get_user_email(cls, user):
        query= '''SELECT * FROM usuarios WHERE email = %s'''
        params = (user.email,)
        result = conn.fetch_one(query, params) 
        conn.close_connection()
        if result is not None:
            return User(
                id = result[0], 
                username = result[1], 
                nombre = result[2], 
                apellido = result[3],
                email = result[4],
                password= result[5],
                fecha_nacimiento = result[6],
                activo= result[7],
                id_insignia = result[9]
                )
        return None 
    
    @classmethod
    def get_users(cls):
        query= '''SELECT * FROM usuarios'''
        results = conn.fetch_all(query) 
        conn.close_connection()
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
                                      activo= result[7],
                                      id_insignia = result[9]))
            return user_list    
        return None 
        
    @classmethod
    def update_user(cls, user):
        query= '''UPDATE usuarios SET username=%s, nombre=%s, apellido=%s, token=%s WHERE id=%s'''
        params=(user.username,user.nombre,user.apellido,user.token,user.id,)
        conn.execute_query(query,params)   
        conn.close_connection()
    
    @classmethod
    def reset_user_pass(cls,user):
        query= '''UPDATE usuarios SET password=%s, token=null WHERE token=%s'''
        params= (user.password,user.token,)
        conn.execute_query(query,params)
        conn.close_connection
        
    @classmethod    
    def edit_password(cls, user):
        query= '''UPDATE usuarios SET password=%s WHERE id=%s'''
        params= (user.password,user.id,)
        conn.execute_query(query,params)
        conn.close_connection
    
    @classmethod
    def activate_user(cls, user):
        query= 'UPDATE usuarios set activo=1, token=null where token=%s'
        params=(user.token,)
        conn.execute_query(query,params)
        conn.close_connection()
        
    @classmethod
    def deactivate_user(cls, user):
        query= '''UPDATE usuarios set activo=0, token=%s WHERE id=%s'''
        params=(user.token,user.id,)
        conn.execute_query(query,params)
        conn.close_connection()