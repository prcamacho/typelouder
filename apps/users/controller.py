from flask import request, render_template, jsonify
from config import Config 
from .models import User
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_mail import Mail
from apps.extensiones import MAIL, load_user
from flask_mail import Message
from flask_login import login_user, logout_user

class UserController:
    @classmethod
    def create_user(cls):
        password= request.form['password']
        token= str(uuid.uuid4())
        password_hash= generate_password_hash(password) 
        user=User(username= request.form['username'],
            nombre= request.form['nombre'],
            apellido= request.form['apellido'],
            email= request.form['email'],
            password= password_hash,
            fecha_nacimiento= request.form['fecha_nacimiento'],
            token= token)
        valid= User.create_user(user)
        print(valid)
        url=str(request.url_root)+'confirmar_email/'+str(token)
        data={
            'url':url,
            'username':user.username,
            'nombre':user.nombre,
            'apellido':user.apellido}
        mensaje=Message('Finaliza tu Registro!!!',sender=Config.CREDENCIALES_EMAIL['email_host_user'], recipients=[user.email]) #configura mail
        mensaje.html= render_template('email/confirmar_mail.html',context=data) 
        MAIL.send(mensaje)
        return jsonify({'message':'Usuario registrado con exito'}, 200)
    
    @classmethod
    def login(cls):
        email = request.form['email']
        password = request.form['password']
        user= User.get_user_email(User(email=email))
        if user and check_password_hash(user.password, password) and user.activo:
            user=load_user(user.id)
            login_user(user)
            return jsonify({'message':'Login exitoso'}, 200)
    
    @classmethod        
    def confirmar_email(cls,token):
        user= User(token=token)
        print(type(user.token))
        User.activate_user(user)   
        return jsonify({'message':'Usuario activado con exito'}, 200) 
     
    @classmethod
    def logout(cls):
        logout_user()
        return jsonify({'message':'Logout exitoso'}, 200)         
    
    @classmethod
    def password_reset(cls):
        email= request.form['email']
        user= User.get_user_email(User(email=email))
        token= str(uuid.uuid4()) #genera un token unico
        user.token= token
        url=str(request.url_root)+'nuevo_password/'+str(token)
        User.update_user(user)
        data={
            'url':url,
            'username':user.username,
            'nombre':user.nombre,
            'apellido':user.apellido}
        mensaje=Message('Recuperar Password',sender=Config.CREDENCIALES_EMAIL['email_host_user'], recipients=[email]) #configura mail
        mensaje.html= render_template('email/recuperar.html',context=data) #renderiza template del mail
        MAIL.send(mensaje)
        return jsonify({'message':'Mensaje para cambio de password enviado con exito'}, 200)
    
    @classmethod
    def nuevo_password(cls, token):
        password = request.form['password']
        password1 = request.form['password1']
        
        if password == password1:
            password_hash = generate_password_hash(password)
            
            query = '''SELECT * FROM usuarios WHERE token=%s'''
            params = (token,)
            
            usuario = conn.fetch_one(query, params)
            
            if usuario:
                query = '''UPDATE usuarios SET password=%s, token=NULL WHERE id=%s'''
                params = (password_hash, usuario['id'])
                conn.execute_query(query, params)
                conn.close_connection()
                
                return redirect(url_for('user.login'))
            else:
                error_message = "Usuario no encontrado. El enlace de restablecimiento de contraseña puede haber caducado."
                return render_template('usuarios/nuevo_password.html',token=token, error_message=error_message)
        else:
            error_message = "Las contraseñas no coinciden. Por favor, asegúrate de ingresar la misma contraseña en ambos campos."
            return render_template('usuarios/nuevo_password.html',token=token, error_message=error_message)