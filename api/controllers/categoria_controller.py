from flask import jsonify
from api.models.categoria_model import Categoria

class CategoriaController:
    
    @classmethod
    def get_categorias(cls):
        categorias= Categoria.get_categorias()
        if categorias is not None:
            lista=[]
            for categoria in categorias:
                lista.append(categoria.serialize())
            return jsonify(lista, 200)
        return jsonify({'message':'No se encontraron categorias'}, 404)