class Config:
    SERVER_NAME= 'localhost:5000'
    DEBUG= True
    TEMPLATE_FOLDER= 'templates/'
    STATIC_FOLDER= 'static/'
    MEDIA_FOLDER= 'media/'
    
    DECENCIALES_DB = {'user': 'root',
                'password': 'Cafayate123',
                'host': 'localhost',
                'database': 'typelouder',
                'port':'3306'}
    
    CREDENCIALES_EMAIL={
    'email_host':"smtp.gmail.com",
    'email_use_tls':True,
    'email_port':587,
    'email_host_user':'byte.force.devs@gmail.com',
    'email_host_password':'noektdyllpwgjdzv'
}
    SECRET_KEY='75958d0dea3aaaf05db37d404e788ff3faaabc733af0560f5f05552a7f6b25de'