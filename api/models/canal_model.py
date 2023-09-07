from api.database import DatabaseConnection as conn
from api.models.servidor_model import Servidor

class Canal:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.id_servidor = kwargs.get('id_servidor')
        self.fecha_creacion = kwargs.get('fecha_creacion') 
    
    def serialize(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'servidor':Servidor.get_servidor_id(Servidor(id=self.id_servidor)).serialize_basico(),
            'fecha_creacion':self.fecha_creacion
        }
    
    @classmethod
    def create_canal(cls, canal):
        query='''INSERT INTO canales(nombre, id_servidor)
                VALUES(%s,%s,%s)'''
        params=(canal.nombre, canal.id_servidor,)
        conn.execute_query(query,params)
        conn.close_connection()        
        
    @classmethod    
    def get_canal(cls, canal):
        query='''SELECT * FROM canales WHERE id=%s'''
        params=(canal.id,)
        result=conn.fetch_one(query,params)
        conn.close_connection()
        if result is not None:
            return Canal(id=result[0], nombre=result[1], id_servidor=result[2], fecha_creacion=result[3])
        return None   
    
    @classmethod    
    def get_canal_servidor(cls, servidor):
        query='''SELECT * FROM canales WHERE id_servidor=%s'''
        params=(servidor.id,)
        results=conn.fetch_all(query,params)
        conn.close_connection()
        if result is not None:
            lista_canales=[]
            for result in results:
                lista_canales.append(Canal(id=result[0], nombre=result[1], id_servidor=result[2], fecha_creacion=result[3]))
            return lista_canales  
        return None  
    
    @classmethod
    def get_canales(cls):
        query='''SELECT * FROM canales'''
        results=conn.fetch_all(query)
        conn.close_connection()
        if results is not None:
            lista_canales=[]
            for result in results:
                lista_canales.append(Canal(id=result[0], nombre=result[1], id_servidor=result[2], fecha_creacion=result[3]))
            return lista_canales    
        return None   
    
    @classmethod
    def update_canal(cls,canal):
        query='''UPDATE canales SET nombre=%s WHERE id=%s'''
        params=(canal.nombre, canal.id,)
        conn.execute_query(query,params)
        conn.close_connection()
    
    @classmethod
    def delete_canal(cls,canal):
        query='''DELETE FROM canales WHERE id=%s'''
        params= (canal.id, )
        conn.execute_query(query, params)
        conn.close_connection()    