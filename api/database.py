import mysql.connector 
from mysql.connector import errors
from config import Config
    
class DatabaseConnection:
    _connection = None
    
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host=Config.CREDENCIALES_DB["host"],
                user=Config.CREDENCIALES_DB["user"],
                port = Config.CREDENCIALES_DB["port"],
                password=Config.CREDENCIALES_DB["password"]
                )
        # if cls._connection is None:
        #     cls._connection = mysql.connector.connect(
        #         host="db4free.net",
        #         user="daniel92",
        #         port = 3306,
        #         password= "Cafayate123"
        #         )    
        return cls._connection    
    
    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute("USE %s" %Config.CREDENCIALES_DB["database"])
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute("USE %s" %Config.CREDENCIALES_DB["database"])
        cursor.execute(query, params)
        results = cursor.fetchall()
        cls.close_connection()
        return results

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute("USE %s" %Config.CREDENCIALES_DB["database"])
        cursor.execute(query,params)
        result = cursor.fetchone()
        cls.close_connection()
        return result

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
    
    @classmethod
    def create_tables(cls):
        crear_database = "CREATE DATABASE IF NOT EXISTS %s" %Config.CREDENCIALES_DB["database"]
        tabla_insignias='''CREATE TABLE IF NOT EXISTS insignias(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR (100) UNIQUE NOT NULL,
                    imagen VARCHAR (255) NOT NULL
                    )'''           
        tabla_usuarios='''CREATE TABLE IF NOT EXISTS usuarios(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR (50) UNIQUE NOT NULL,
                    nombre VARCHAR (100) NOT NULL,
                    apellido VARCHAR (100) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    activo TINYINT NOT NULL DEFAULT(0),
                    token VARCHAR(100),
                    id_insignia INT,
                    FOREIGN KEY (id_insignia) REFERENCES insignias(id)  
                    )'''
        tabla_categorias='''CREATE TABLE IF NOT EXISTS categorias(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR (100) UNIQUE NOT NULL,
                    imagen VARCHAR (255) NOT NULL 
                    )'''        
        tabla_servidores='''CREATE TABLE IF NOT EXISTS servidores(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR (100) UNIQUE NOT NULL,
                    descripcion TEXT NOT NULL,
                    imagen VARCHAR (255) NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT NOW(),
                    privado TINYINT NOT NULL DEFAULT(0),
                    password VARCHAR(255),
                    token VARCHAR(100),
                    id_usuario_creador INT NOT NULL,
                    id_categoria INT NOT NULL,
                    FOREIGN KEY (id_usuario_creador) REFERENCES usuarios(id) ON DELETE CASCADE,
                    FOREIGN KEY (id_categoria) REFERENCES categorias(id)  
                    )'''
        tabla_miembros='''CREATE TABLE IF NOT EXISTS miembros(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    id_usuario INT NOT NULL,
                    id_servidor INT NOT NULL,
                    fecha_union TIMESTAMP DEFAULT NOW(),
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE,
                    FOREIGN KEY (id_servidor) REFERENCES servidores(id) ON DELETE CASCADE  
                    )'''
        tabla_canales='''CREATE TABLE IF NOT EXISTS canales(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR (100) NOT NULL,
                    id_servidor INT NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT NOW(),
                    FOREIGN KEY (id_servidor) REFERENCES servidores(id) ON DELETE CASCADE  
                    )'''
        # tabla mensaje queda a revision, para agregar contenido multimedia
        tabla_mensajes='''CREATE TABLE IF NOT EXISTS mensajes(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    id_canal INT NOT NULL,
                    id_usuario INT NOT NULL,
                    mensaje TEXT NOT NULL,
                    fecha_mensaje TIMESTAMP DEFAULT NOW(),
                    FOREIGN KEY (id_canal) REFERENCES canales(id) ON DELETE CASCADE,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE 
                    )'''
        tabla_reacciones='''CREATE TABLE IF NOT EXISTS reacciones(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    id_mensaje INT NOT NULL,
                    id_usuario INT NOT NULL,
                    reaccion TINYINT DEFAULT(NULL),
                    FOREIGN KEY (id_mensaje) REFERENCES mensajes(id) ON DELETE CASCADE,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE 
                    )'''
                    
        try:
            cursor = cls.get_connection().cursor()
        #     # Establece max_allowed_packet en 1 GB (1073741824 bytes)
        #     cursor.execute("SET GLOBAL max_allowed_packet=1073741824;")

        # # Establece wait_timeout en 300 segundos (5 minutos)
        #     cursor.execute("SET GLOBAL wait_timeout = 300;")
            cursor.execute(crear_database)
            cursor.execute("USE %s" %Config.CREDENCIALES_DB["database"])
            cursor.execute(tabla_insignias)
            cursor.execute(tabla_usuarios)
            cursor.execute(tabla_categorias)
            cursor.execute(tabla_servidores)
            cursor.execute(tabla_miembros)
            cursor.execute(tabla_canales)
            cursor.execute(tabla_mensajes)
            cursor.execute(tabla_reacciones)
            cls.close_connection()
        except errors.DatabaseError as err:
            print("Error al conectar o crear la base de datos.", err)
            raise

def cargar_datos():
    DatabaseConnection.execute_query("""INSERT INTO insignias (nombre, imagen) VALUES
                                    ('Insignia 1', 'imagen1.png'),
                                    ('Insignia 2', 'imagen2.png'),
                                    ('Insignia 3', 'imagen3.png')""")
    DatabaseConnection.execute_query("""INSERT INTO usuarios (username, nombre, apellido, email, password, fecha_nacimiento, activo, id_insignia) VALUES
                                    ('usuario1', 'Nombre Usuario 1', 'Apellido Usuario 1', 'usuario1@example.com', 'contraseña1', '2000-01-01', 1, 1),
                                    ('usuario2', 'Nombre Usuario 2', 'Apellido Usuario 2', 'usuario2@example.com', 'contraseña2', '1995-05-10', 1, 2),
                                    ('usuario3', 'Nombre Usuario 3', 'Apellido Usuario 3', 'usuario3@example.com', 'contraseña3', '1988-11-15', 1, 3)""")
    DatabaseConnection.execute_query("""INSERT INTO categorias (nombre, imagen) VALUES
                                    ('Categoría 1', 'imagen_cat1.png'),
                                    ('Categoría 2', 'imagen_cat2.png'),
                                    ('Categoría 3', 'imagen_cat3.png')""")
    DatabaseConnection.execute_query("""INSERT INTO servidores (nombre, imagen, descripcion, privado, id_usuario_creador, id_categoria) VALUES
                                    ('Servidor 1', 'imagen_serv1.png', 'Descripción del servidor 1', 0, 1, 1),
                                    ('Servidor 2', 'imagen_serv2.png', 'Descripción del servidor 2', 1, 2, 2),
                                    ('Servidor 3', 'imagen_serv3.png', 'Descripción del servidor 3', 0, 3, 3)""")
    DatabaseConnection.execute_query("""INSERT INTO miembros (id_usuario, id_servidor) VALUES
                                    (1, 1),
                                    (2, 1),
                                    (3, 2)""")
    DatabaseConnection.execute_query("""INSERT INTO canales (nombre, id_servidor) VALUES
                                    ('Canal 1', 1),
                                    ('Canal 2', 1),
                                    ('Canal 3', 2)""")
    DatabaseConnection.execute_query("""INSERT INTO mensajes (id_canal, id_usuario, mensaje) VALUES
                                    (1, 1, 'Mensaje del usuario 1 en Canal 1'),
                                    (1, 2, 'Mensaje del usuario 2 en Canal 1'),
                                    (2, 3, 'Mensaje del usuario 3 en Canal 2')""")
    DatabaseConnection.execute_query("""INSERT INTO reacciones (id_mensaje, id_usuario, reaccion) VALUES
                                    (1, 1, 1),
                                    (1, 2, 2),
                                    (2, 3, 1)""")
    
    
    