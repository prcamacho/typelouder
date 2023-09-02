from api.database import DatabaseConnection as conn

class Servidor:
    def __init__(self,id=None, nombre=None, descripcion=None, imagen=None, fecha_creacion=None, 
                privado=None, password=None, token=None, id_usuario_creador=None, id_categoria=None):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.imagen=imagen
        self.fecha_creacion=fecha_creacion
        self.privado=privado
        self.password=password
        self.token=token
        self.id_usuario_creador=id_usuario_creador
        self.id_categoria=id_categoria
    
    @classmethod
    def create_servidor(cls, servidor):
        query='''INSERT INTO servidores(nombre, descripcion, imagen, 
                privado, password, token, id_usuario_creador, id_categoria)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
        params=(servidor.nombre, servidor.descripcion, servidor.imagen,
                servidor.privado, servidor.password, servidor.token, 
                servidor.id_usuario_creador, servidor.id_categoria)
        conn.execute_query(query,params)
        conn.close_connection()        
        
    @classmethod    
    def get_servidor(cls, servidor):
        query='''SELECT * FROM servidores WHERE token=%s'''
        params=(servidor.token,)
        result=conn.fetch_one(query,params)
        conn.close_connection()
        if result is not None:
            return Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                            imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                            token=result[7], id_usuario_creador=result[8], id_categoria=result[9])
        return None   
    
    @classmethod
    def get_servidores(cls):
        query='''SELECT * FROM servidores'''
        results = conn.fetch_all(query)
        conn.close_connection()
        if results is not None:
            lista_servidores=[]
            for result in results:
                lista_servidores.append(Servidor(id=result[0], nombre=result[1], descripcion=result[2],
                            imagen=result[3], fecha_creacion=result[4], privado=result[5], password=result[6],
                            token=result[7], id_usuario_creador=result[8], id_categoria=result[9]))
            return lista_servidores    
        return None   
    
    @classmethod
    def update_servidor(cls,servidor):
        query='''UPDATE servidores SET nombre=%s, descripcion=%s, imagen=%s, privado=%s, password=%s
        WHERE token=%s and id_usuario_creador=%s'''
        params=(servidor.nombre, servidor.descripcion, servidor.imagen, servidor.privado,
                servidor.password, servidor.token, servidor.id_usuario_creador,)
        conn.execute_query(query,params)
        conn.close_connection()
    
    @classmethod
    def delete_servidor(cls,servidor):
        query= '''DELETE FROM servidores WHERE token=%s AND id_usuario_creador=%s'''
        params= (servidor.token, servidor.id_usuario_creador,)
        conn.execute_query(query,params)
        conn.close_connection()