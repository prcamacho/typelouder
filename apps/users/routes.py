from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config 
import uuid
from flask_mail import Message
from apps.conector import DatabaseConnection as conn
from apps.extensiones import MAIL, load_user
from flask_login import login_user, logout_user, current_user
from .controller import UserController

app_usuario= Blueprint('user', __name__) 

app_usuario.route('/registro', methods=['POST'])(UserController.create_user())
