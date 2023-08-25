from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from apps.database import DatabaseConnection as conn
import uuid

app_servidor= Blueprint('servidor', __name__)

@app_servidor.route('/nuevo_servidor',methods=['GET','POST'])
@login_required
def nuevo_servidor():
    if request.method == 'POST':
        nombre= request.form['nombre']
        imagen= request.form['imagen']
        descripcion= request.form['descripcion']
        privado= request.form['privado']
        password= request.form['password']
        token= uuid.uuid4()
        id_usuario= current_user.id
        categoria= request.form['categoria']
        query='''INSERT INTO servidores (nombre, imagen, descripcion, privado, password, token, id_usuario_creador, id_categoria)
        values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        params=(nombre,imagen,descripcion,privado,generate_password_hash(password),token,id_usuario,categoria,)
        conn.execute_query(query,params,)
        return redirect(url_for('home'))
    return render_template('servidores/nuevo.html')

@app_servidor.route('/eliminar/<int:id>')
def eliminar_servidor(id):
    query='''SELECT * FROM servidores WHERE id=%s'''
    params=(id,)
    servidor= conn.fetch_one(query,params)
    if servidor[8] == current_user.id:
        q_id_canal='''SELECT id FROM canales WHERE id=%s'''
        conn.fetch_all(q_id_canal,(id,))
        
        query='''DELETE FROM servidores WHERE id=%s'''
        conn.execute_query(query,(id,))
        
    
    