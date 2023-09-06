from flask_login import UserMixin
from api.database import DatabaseConnection as conn

class User(UserMixin):
    def __init__(self,id=None,username=None,nombre=None,apellido=None,email=None,password=None,fecha_nacimiento=None,activo=False,token=None,id_insignia=None):
        self.id=id
        self.username=username
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password
        self.fecha_nacimiento=fecha_nacimiento
        self.activo=activo
        self.token=token
        self.id_insignia=id_insignia
    
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
                id_insignia = result[8]
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
                id_insignia = result[8]
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
                user_list.append(User(id = result[0], username = result[1], nombre = result[2], apellido = result[3],email = result[4],fecha_nacimiento = result[6],id_insignia = result[8]))
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