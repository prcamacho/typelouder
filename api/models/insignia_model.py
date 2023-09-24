from api.database import DatabaseConnection as conn

class Insignia:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.imagen = kwargs.get('imagen')
        
    def serialize(self):
        return self.__dict__
        
    
    @classmethod
    def get_insignia(cls, insignia):
        query= '''SELECT * FROM insignias WHERE id =%s'''   
        params= (insignia.id,)
        insignia = conn.fetch_one(query,params)
        if insignia:
            return Insignia(id=insignia[0],nombre=insignia[1],imagen=insignia[2])
        return None
    