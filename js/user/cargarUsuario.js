function cargarUsuario(){
    fetch("http://127.0.0.1:8000/users/", {
    method: "GET",
    credentials: "include"
        })
    .then(response => response.json())
    .then(data => {
        const username = document.querySelector('.username-card');
        const nombre = document.querySelector('.nombre-apellido-card');
        const email = document.querySelector('.email-card');

        const useruser = document.querySelector('.username-usuario');
        useruser.id = data.id;
        const nombre_apellido = document.querySelector('.nombre-usuario');

        username.textContent = data.username;
        nombre.textContent = data.nombre+" "+data.apellido;
        email.textContent = data.email;

        useruser.textContent = data.username;
        nombre_apellido.textContent = data.nombre+" "+data.apellido;
            })
    .catch(error => {
        console.error('Hubo un problema con la solicitud:', error);
        });
    }

export { cargarUsuario }    