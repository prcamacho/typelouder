from api.database import DatabaseConnection as conn
from api.models.user_model import User
from api.models.servidor_model import Servidor

class Miembro:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.id_usuario = kwargs.get('id_usuario')
        self.id_servidor = kwargs.get('id_servidor')
        self.fecha_union = kwargs.get('fecha_union')
        
    def serialize(self):
        return {
            'id':self.id,
            'usuario':User.get_user(User(id=self.id_usuario)).serialize_basico(),
            'servidor':Servidor.get_servidor_id(Servidor(id=self.id_servidor)).serialize_basico(),
            'fecha_union': self.fecha_union
        }
    
    @classmethod
    def unirse_servidor(cls, miembro):
        query= 'INSERT INTO miembros (id_usuario, id_servidor) values(%s,%s)'
        params= (miembro.id_usuario, miembro.id_servidor,)
        conn.execute_query(query,params)
        conn.close_connection()
        
    @classmethod
    def salir_servidor(cls, miembro):
        query= 'DELETE FROM miembros WHERE id_usuario=%s AND id_servidor=%s'
        params= (miembro.id_usuario, miembro.id_servidor,)
        conn.execute_query(query,params)
        conn.close_connection()    