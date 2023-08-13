from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config 
import uuid
from flask_mail import Message
from apps import mail, login_manager
from apps.conector import DatabaseConnection as conn
from flask_login import login_user,UserMixin, logout_user

class User(UserMixin):
    pass

app_usuario= Blueprint('usuario', __name__)

@app_usuario.route('/')
def hello():
    return 'Hola mundo!'    

@login_manager.user_loader
def load_user(user_id):
    query="SELECT * FROM usuarios WHERE id = %s", (user_id,)
    cursor = conn.fetch_one(query,(user_id,))
    user_data = cursor.fetchone()
    conn.close_connection()
    if user_data:
        user = User()
        user.id = user_data['id']
        return user
    return None


@app_usuario.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        query='SELECT * FROM usuarios where email=%s'
        params=(email,)
        result=conn.fetch_one(query,params)[0]
        if result and check_password_hash(result[0][5], password):
            user=User()
            user.id=result[0][0]
            return redirect('home/index.html')
        else:
            return 'Credenciales incorrectas'
    return render_template('usuarios/login.html')

@app_usuario.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

#registra un usuario, y envia un mail para validar email
@app_usuario.route('/registro', methods=['POST'])
def register():
    token= uuid.uuid4() #genera un token unico
    url='http://'+request.META['HTTP_HOST']+'/confirmar_mail/'+str(token)
    password= request.form['password'] #obtener password del formulario
    email= request.form['email'] #obtener email del form
    password_hash= generate_password_hash(password) #encripta password
    mensaje=Message('Finaliza tu Registro!!!',sender=Config.CREDENCIALES_EMAIL['email_host_user'], recipients=[email]) #configura mail
    data={} #configurar diccionario para pasar informacion al template del mail
    mensaje.html= render_template('email/confirmar_email.html',context=data) #renderiza template del mail
    mail.send(mensaje) # envia mail
    pass

# confirma el email del usuario cambiando su estado a activo=True
@app_usuario.route('/confirmar_mail/<token>')
def confirmar_email():
    '''escribir query que actualice el usuario buscando por el token
    que cambie de activo = 0 a activo = 1 y vuelva el token a null'''
    query= 'UPDATE usuarios set activo=1, token=null where token=%s'
    # luego redirigir a login o iniciar sesion directamente
    pass

def reset_password():
    pass

