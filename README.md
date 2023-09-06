# typelouder
Proyecto Final para Programación 2 

Descripción corta del proyecto y su propósito.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Rutas](#rutas)
- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Introducción

Proyecto similar a Discord

## Rutas

El proyecto proporciona las siguientes rutas:


### Rutas relacionadas con Canales

- **`/crear_canal` (Método POST)**: Crea un nuevo canal.
  - **Campos obligatorios**:
    - `nombre`: Nombre del canal.
    - `token_servidor`: Token del servidor al que pertenece el canal.

- **`/canales/<token_servidor>` (Método GET)**: Obtiene los canales de un servidor específico.
  - **Campos obligatorios**:
    - `token_servidor`: Token del servidor.

- **`/canales_all` (Método GET)**: Obtiene todos los canales.

- **`/editar_canal/<int:id>` (Método PUT)**: Actualiza un canal existente.
  - **Campos obligatorios**:
    - `id`: Identificador del canal.
    - `nombre`: Nuevo nombre del canal.

- **`/eliminar_canal/<int:id>` (Método DELETE)**: Elimina un canal.
  - **Campos obligatorios**:
    - `id`: Identificador del canal.

### Rutas relacionadas con Mensajes

- **`/crear_mensaje` (Método POST)**: Crea un nuevo mensaje.
  - **Campos obligatorios**:
    - `mensaje`: Contenido del mensaje.
    - `id_canal`: ID del canal al que se envía el mensaje.

- **`/mensajes/<int:id>` (Método GET)**: Obtiene un mensaje específico.
  - **Campos obligatorios**:
    - `id`: Identificador del mensaje.

- **`/mensajes/<canal>` (Método GET)**: Obtiene mensajes de un canal específico.
  - **Campos obligatorios**:
    - `canal`: Nombre del canal.

- **`/editar_mensaje` (Método PUT)**: Actualiza un mensaje existente.
  - **Campos obligatorios**:
    - `id`: Identificador del mensaje.
    - `mensaje`: Nuevo contenido del mensaje.

- **`/eliminar_mensaje/<int:id>` (Método DELETE)**: Elimina un mensaje.
  - **Campos obligatorios**:
    - `id`: Identificador del mensaje.

- **`/reaccionar/<int:id_mensaje>` (Método POST)**: Agrega una reacción a un mensaje.
  - **Campos obligatorios**:
    - `raccion`: Reacción del mensaje (booleano, `true` o `false`).

- **`/editar_reaccion/<int:id>` (Método PUT)**: Actualiza una reacción de mensaje.
  - **Campos obligatorios**:
    - `id`: Identificador de la reacción.


### Rutas relacionadas con Servidores

- **`/crear_servidor` (Método POST)**: Crea un nuevo servidor.
  - **Campos obligatorios**:
    - `nombre`: Nombre del servidor.
    - `descripcion`: Descripción del servidor.
    - `imagen`: Imagen del servidor.
    - `privado`: Indicador de servidor privado.
    - `id_categoria`: ID de la categoría del servidor.

- **`/servidores` (Método GET)**: Obtiene servidores públicos.

- **`/servidores_all` (Método GET)**: Obtiene todos los servidores.

- **`/update_servidor/<token>` (Método PUT)**: Actualiza un servidor existente.
  - **Campos obligatorios**:
    - `token`: Token del servidor.
    - `nombre`: Nuevo nombre del servidor.
    - `descripcion`: Nueva descripción del servidor.
    - `imagen`: Nueva imagen del servidor.
    - `privado`: Nuevo indicador de servidor privado.

- **`/delete_servidor/<token>` (Método DELETE)**: Elimina un servidor.
  - **Campos obligatorios**:
    - `token`: Token del servidor.


### Rutas relacionadas con Usuarios

- **`/registro` (Método POST)**: Registra un nuevo usuario.
  - **Campos obligatorios**:
    - `username`: Nombre de usuario.
    - `nombre`: Nombre del usuario.
    - `apellido`: Apellido del usuario.
    - `email`: Correo electrónico del usuario.
    - `password`: Contraseña del usuario.
    - `fecha_nacimiento`: Fecha de nacimiento del usuario.

- **`/login` (Método POST)**: Inicia sesión de usuario.
  - **Campos obligatorios**:
    - `email`: Correo electrónico del usuario.
    - `password`: Contraseña del usuario.

- **`/confirmar_email/<token>` (Método GET)**: Confirma el correo electrónico del usuario.
  - **Campos obligatorios**:
    - `token`: Token de confirmación.

- **`/logout` (Método GET)**: Cierra sesión del usuario.

- **`/password_reset` (Método POST)**: Inicia el proceso de restablecimiento de contraseña.
  - **Campos obligatorios**:
    - `email`: Correo electrónico del usuario.

- **`/nuevo_password/<token>` (Método PUT)**: Establece una nueva contraseña para el usuario.
  - **Campos obligatorios**:
    - `token`: Token de restablecimiento de contraseña.
    - `password`: Nueva contraseña.
    - `password1`: Confirmación de la nueva contraseña.

- **`/editar_usuario` (Método PUT)**: Actualiza la información del usuario.
  - **Campos obligatorios**:
    - `username`: Nuevo nombre de usuario.
    - `nombre`: Nuevo nombre del usuario.
    - `apellido`: Nuevo apellido del usuario.

- **`/editar_password` (Método PUT)**: Cambia la contraseña del usuario.
  - **Campos obligatorios**:
    - `password1`: Contraseña actual del usuario.
    - `password2`: Nueva contraseña.
    - `password3`: Confirmación de la nueva contraseña.

- **`/desactivar_cuenta` (Método PUT)**: Desactiva la cuenta del usuario.

- **`/activar_cuenta/<token>` (Método GET)**: Activa la cuenta del usuario.
  - **Campos obligatorios**:
    - `token`: Token de activación.

- **`/usuarios/<int:id>` (Método GET)**: Obtiene información de un usuario específico.
  - **Campos obligatorios**:
    - `id`: Identificador del usuario.

- **`/usuarios` (Método GET)**: Obtiene una lista de todos los usuarios.

## Requisitos

Tener instalado en el Python 3.9 o superior.
Puedes instalar todas las dependencias ejecutando el siguiente comando desde dentro del proyecto:
pip install -r requirements.txt

## Configuración

Para configurar el entorno de desarrollo y ejecutar este proyecto, sigue los siguientes pasos:

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local utilizando el siguiente comando de git:

git clone https://github.com/prcamacho/typelouder.git

### 2. Configurar Variables de Entorno

Crea un archivo de variables de entorno `.env` en la raíz del proyecto y configura las variables necesarias. 

A continuación, se muestra un ejemplo de cómo puedes configurar las variables en el archivo `.env`:

# Archivo .env

# Configuración de la base de datos
DATABASE_URL=sqlite:///mydatabase.db
SECRET_KEY=mi_clave_secreta
DEBUG=True

# Ejecutar la aplicación
python run.py

## Contribución

Gustavo Paredez, Gastón Gonzalez, Pablo Camacho y Daniel Chachagua
