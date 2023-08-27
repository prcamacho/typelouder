from apps.database import DatabaseConnection as conn

class Mensaje:
    def __init__(self,id=None, id_usuario=None, id_canal=None, mensaje=None, fecha_mensaje=None):
        self.id=id
        self.id_usuario=id_usuario
        self.id_canal=id_canal
        self.mensaje=mensaje
        self.fecha_mensaje=fecha_mensaje
    
    @classmethod
    def create_mensaje(cls, mensaje):
        query='''INSERT INTO mensajes(id_usuario, id_canal, mensaje, fecha_mensaje)
                VALUES(%s,%s,%s,%s)'''
        params=(mensaje.id_usuario, mensaje.id_canal, mensaje.mensaje, mensaje.fecha_mensaje,)
        conn.execute_query(query,params)
        conn.close_connection()        
        
    @classmethod    
    def get_mensaje(cls, mensaje):
        query='''SELECT * FROM mensajes WHERE id=%s'''
        params=(mensaje.id,)
        result=conn.fetch_one(query,params)
        conn.close_connection()
        if result is not None:
            return Mensaje(id=result[0], id_usuario=result[1], id_canal=result[2], mensaje=result[3], fecha_mensaje=result[4])
        return None   
    
    @classmethod    
    def get_mensaje_canal(cls, canal):
        query='''SELECT * FROM mensajes WHERE id_canal=%s'''
        params=(canal.id,)
        results=conn.fetch_all(query,params)
        conn.close_connection()
        if result is not None:
            lista_servidores=[]
            for result in results:
                lista_servidores.append(Mensaje(id=result[0], id_usuario=result[1], id_canal=result[2], mensaje=result[3], fecha_mensaje=result[4]))
            return lista_servidores  
        return None  
    
    @classmethod
    def get_mensajes(cls):
        query='''SELECT * FROM mensajes'''
        results=conn.fetch_all(query)
        conn.close_connection()
        if results is not None:
            lista_servidores=[]
            for result in results:
                lista_servidores.append(Mensaje(id=result[0], id_usuario=result[1], id_canal=result[2], mensaje=result[3], fecha_mensaje=result[4]))
            return lista_servidores    
        return None   
    
    @classmethod
    def update_mensaje(cls,mensaje):
        query='''UPDATE mensajes SET mensaje=%s WHERE id=%s'''
        params=(mensaje.id,)
        conn.execute_query(query,params)
        conn.close_connection()
    
    @classmethod
    def delete_servidor(cls,mensaje):
        query='''DELETE FROM mensajes WHERE id=%s AND id_usuario=%s'''
        params= (mensaje.id, mensaje.id_usuario,)
        conn.execute_query(query, params)
        conn.close_connection()