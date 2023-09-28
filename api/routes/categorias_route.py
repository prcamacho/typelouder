from flask import Blueprint
from api.controllers.categoria_controller import CategoriaController

app_categoria= Blueprint('categoria', __name__, url_prefix='/categorias')

app_categoria.route('/all',methods=['GET'])(CategoriaController.get_categorias)
