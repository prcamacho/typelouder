from flask import Blueprint
from config import Config 

app_usuario= Blueprint('usuario', __name__)

@app_usuario.route('/')
def hello():
    return 'Hola mundo!'    

@app_usuario.route('/login/')
def login():
    pass

def logout():
    pass

def register():
    pass

def reset_password():
    pass

