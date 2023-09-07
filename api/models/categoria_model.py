from api.database import DatabaseConnection as conn

class Categoria:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.imagen = kwargs.get('imagen')
        
    def serialize(self):
        return self.__dict__
    
    @classmethod
    def get_categoria(cls, categoria):
        query= '''SELECT * FROM categorias WHERE id =%s'''   
        params= (categoria.id,)
        categoria = conn.fetch_one(query,params)
        conn.close_connection()
        if categoria:
            return Categoria(id=categoria[0],nombre=categoria[1],imagen=categoria[2])
        return None