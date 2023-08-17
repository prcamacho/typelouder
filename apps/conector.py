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
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute("USE %s" %Config.CREDENCIALES_DB["database"])
        cursor.execute(query, params)
        return cursor.fetchone()

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
    
    @classmethod
    def create_tables(cls):
        crear_database = "CREATE DATABASE IF NOT EXISTS %s" %Config.CREDENCIALES_DB["database"]
        tabla_usuarios='''CREATE TABLE IF NOT EXISTS usuarios(
                    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR (50) UNIQUE NOT NULL,
                    nombre VARCHAR (100) NOT NULL,
                    apellido VARCHAR (100) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    activo TINYINT NOT NULL DEFAULT(0),
                    token VARCHAR(100)  
                    )'''
        try:
            cursor = cls.get_connection().cursor()
            cursor.execute(crear_database)
            cursor.execute("USE %s" %Config.CREDENCIALES_DB["database"])
            cursor.execute(tabla_usuarios)
            cls.close_connection()
        except errors.DatabaseError as err:
            print("Error al conectar o crear la base de datos.", err)
            raise

