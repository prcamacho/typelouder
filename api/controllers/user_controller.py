from flask import request, render_template, jsonify, make_response, url_for
from config import Config 
from ..models.user_model import User
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from api.extensiones import MAIL, load_user
from flask_mail import Message
from flask_login import login_user, logout_user, current_user
from api.models.imagen_model import Imagen

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
        User.create_user(user)
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
        response = make_response(jsonify({'message': 'Login successful'}))
        response.set_cookie('authenticated', 'true')
        #if user and check_password_hash(user.password, password) and user.activo:
        if user and check_password_hash(user.password, password):
            user=load_user(user.id)
            login_user(user)
            return response
        

    @classmethod        
    def confirmar_email(cls,token):
        user= User(token=token)
        User.activate_user(user)   
        return jsonify({'message':'Usuario activado con exito'}, 200) 

    @classmethod
    def logout(cls):
        logout_user()
        response = make_response(jsonify({'message': 'Logout successful'}))
        response.set_cookie('authenticated', '', expires=0)
        return response        
    
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
            user= User(token=token, password=password_hash)
            User.reset_user_pass(user)
            return jsonify({'message':'Password reseteado con éxito!'})
        
    @classmethod
    def edit_user(cls):
        username= request.form['username']
        nombre= request.form['nombre']
        apellido= request.form['apellido'] 
        imagen= request.files['imagen']
        filename = Imagen.guardar_imagen(imagen,request,Config.MEDIA_USER,(250,250))
        user= User(id=current_user.id,username=username,nombre=nombre,apellido=apellido, imagen=filename)
        User.update_user(user)
        return jsonify({'message':'Usuario actualizado con éxito!'},200)
        
    @classmethod
    def edit_password(cls):
        pass1= request.form['password1']
        pass2= request.form['password2']
        pass3= request.form['password3']
        user_pass= User.get_user(User(id=current_user.id))
        if check_password_hash(user_pass.password,pass1):
            if pass2==pass3:
                user= User(id=user_pass.id,password=generate_password_hash(pass2))
                User.edit_password(user)
                return jsonify({'message':'Password editado correctamente'}) 
            return jsonify({'message':'Los passwords no coinciden'})   
        return jsonify({'message':'Password actual incorrecto'})    
    
    @classmethod
    def desactivar_cuenta(cls):
        token= str(uuid.uuid4()) #genera un token unico
        user=User(id=current_user.id,username=current_user.username,nombre=current_user.nombre,apellido=current_user.apellido,email=current_user.email, token=token)
        url=str(request.url_root)+'activar_cuenta/'+str(token)
        User.update_user(user)
        data={
            'url':url,
            'username':user.username,
            'nombre':user.nombre,
            'apellido':user.apellido}
        mensaje=Message('Regresa pronto!!!',sender=Config.CREDENCIALES_EMAIL['email_host_user'], recipients=[user.email]) #configura mail
        mensaje.html= render_template('email/activar_cuenta.html',context=data) #renderiza template del mail
        User.deactivate_user(user)
        MAIL.send(mensaje)
        return jsonify({'message':'Cuenta desactivada!'})
    
    @classmethod
    def activar_cuenta(cls, token):
        user= User(token=token)
        User.activate_user(user)   
        return jsonify({'message':'Usuario activado con exito'}, 200) 
    
    @classmethod
    def usuario(cls):
        user= User.get_user(User(id=current_user.id))
        if user is not None:
            user_data=user.serialize()
            #user_data['imagen'] =  str(request.url_root)+url_for(endpoint='media.imagen_media_user', filename= user_data['imagen'])
            return jsonify(user_data)
        return jsonify({'message':'Usuario no encontrado'}) 
    
    @classmethod
    def lista_usuarios(cls):
        users= User.get_users()
        lista=[]
        for user in users:
            user_data=user.serialize()
            #user_data['imagen'] =  str(request.url_root)+url_for(endpoint='media.imagen_media_user', filename= user_data['imagen'])
            lista.append(user_data)
        return jsonify(lista , 200)    
            
         