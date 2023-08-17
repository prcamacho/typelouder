from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config 
import uuid
from flask_mail import Message
from apps.conector import DatabaseConnection as conn
from apps.extensiones import MAIL, load_user
from flask_login import login_user, logout_user

app_usuario= Blueprint('user', __name__) 


#registra un usuario, y envia un mail para validar email
@app_usuario.route('/registro', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #obtener datos del formulario
        username= request.form['username']
        nombre= request.form['nombre']
        apellido= request.form['apellido']
        email= request.form['email']
        password= request.form['password']
        fecha_nacimiento= request.form['fecha_nacimiento']
        #encripta password
        password_hash= generate_password_hash(password) 
        token= uuid.uuid4() #genera un token unico
        url=str(request.url_root)+'confirmar_mail/'+str(token) #url para la activacion de la cuenta
        data={
            'url':url,
            'username':username,
            'nombre':nombre,
            'apellido':apellido}
        mensaje=Message('Finaliza tu Registro!!!',sender=Config.CREDENCIALES_EMAIL['email_host_user'], recipients=[email]) #configura mail
        mensaje.html= render_template('email/confirmar_mail.html',context=data) #renderiza template del mail
        MAIL.send(mensaje) # envia mail
        #coneccion y registro a la base de datos 
        query='''INSERT INTO usuarios (username, nombre, apellido,email,password,fecha_nacimiento,token) values (%s,%s,%s,%s,%s,%s,%s)'''
        params= (username,nombre,apellido,email,password_hash,fecha_nacimiento,str(token),)
        conn.execute_query(query,params)
        conn.close_connection()
        return redirect(url_for('user.login'))
    return render_template('usuarios/registro.html')


@app_usuario.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        query='SELECT * FROM usuarios where email=%s'
        params=(email,)
        result=conn.fetch_one(query,params)
        if result and check_password_hash(result[5], password) and result[7]:
            user=load_user(result[0])
            login_user(user)
            return redirect('/')
        else:
            return render_template('usuarios/login.html')   
    return render_template('usuarios/login.html')

@app_usuario.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app_usuario.route('/confirmar_mail/<token>')
def confirmar_email(token):
    '''confirma el email del usuario cambiando su estado a activo=True'''
    query= 'UPDATE usuarios set activo=1, token=null where token=%s'
    params=(token,)
    conn.execute_query(query,params)
    conn.close_connection()
    return redirect(url_for('user.login'))

def reset_password():
    pass
