import os
from PIL import Image
from werkzeug.utils import secure_filename

class Imagen:
    @classmethod
    def nombre_unico_imagen(cls, filename, carpeta):
        if not os.path.exists(os.path.join(carpeta, filename)):
            return filename
        nombre, extension = os.path.splitext(filename)
        cont = 1
        nuevo_nombre = f"{nombre}_{cont}{extension}"
        while os.path.exists(os.path.join(carpeta, nuevo_nombre)):
            cont += 1
            nuevo_nombre = f"{nombre}_{cont}{extension}"
        return nuevo_nombre

    @classmethod
    def guardar_imagen(cls, imagen, solicitud, carpeta, dimension:tuple):
        if 'imagen' not in solicitud.files:
            return 'No se ha proporcionado una imagen en la solicitud', 400
        filename = secure_filename(imagen.filename) 
        # if imagen.filename == '':
        #     return 'El nombre del archivo no es válido', 400
        filename = cls.nombre_unico_imagen(imagen.filename, carpeta)
        imagen= Image.open(imagen)
        imagen.thumbnail(dimension)
        imagen.save(os.path.join(carpeta, filename))
        return filename 
    
    @classmethod
    def delete_image(cls,carpeta,filename):
        media_path = os.path.join(carpeta, filename)
        if os.path.exists(media_path):
                os.remove(media_path)