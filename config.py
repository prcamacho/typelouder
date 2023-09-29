import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG= True
    TEMPLATE_FOLDER= '../templates/'
    STATIC_FOLDER= 'static'
    MEDIA_FOLDER= 'media'
    MEDIA_SERVIDOR= 'media/servidores'
    MEDIA_USER = 'media/users'
    
    PORT=8000
    
    CREDENCIALES_DB = {'user': os.getenv("database_user"),
                'password': os.getenv("database_password"),
                'host': os.getenv("database_host"),
                'database': os.getenv("database_name"),
                'port':os.getenv("database_port")}   
    
    SECRET_KEY = os.getenv("secret_key")
    
    CREDENCIALES_EMAIL={
    'email_host':os.getenv('email_host'),
    'email_use_tls':os.getenv('email_use_tls'),
    'email_port':os.getenv('email_port'),
    'email_host_user':os.getenv('email_host_user'),
    'email_host_password':os.getenv('email_host_password')
    }