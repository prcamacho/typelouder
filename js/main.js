document.addEventListener("DOMContentLoaded", function () {
    // Realizar una solicitud GET al servidor cuando la página se carga

    var tituloServidor = document.querySelector(".contenedor-titulo");
    var popupServidor = document.querySelector(".popup-servidor");
    var imagenFlecha = document.querySelector(".flecha");
    var popupVisible = false;

    tituloServidor.addEventListener('click', function() {
    popupVisible = !popupVisible;
    popupServidor.style.display = popupVisible ? 'block' : 'none';
    imagenFlecha.style.transition = 'transform 0.3s ease-in-out';
    // popupServidor.style.transform = popupVisible ? 'translateY(0)' : 'translateY(-100%)';
    imagenFlecha.style.transform = popupVisible ? 'rotateZ(180deg)' : 'rotateZ(0deg)';
    setTimeout(function() {
        imagenFlecha.style.transition = '';
    }, 300);
    });


    
    var contenedorUsuario = document.querySelector(".contenedor-usuario");
    var popupUsuario = document.querySelector(".popup-usuario");
    var imagenFlechaUsuario = document.querySelector(".flecha-usuario");
    var popupVisibleUsuario = false;

    contenedorUsuario.addEventListener('click', function() {
    popupVisibleUsuario = !popupVisibleUsuario;
    popupUsuario.style.display = popupVisibleUsuario ? 'block' : 'none';
    imagenFlechaUsuario.style.transition = 'transform 0.3s ease-in-out';
    // popupServidor.style.transform = popupVisible ? 'translateY(0)' : 'translateY(-100%)';
    imagenFlechaUsuario.style.transform = popupVisibleUsuario ? 'rotateZ(0deg)' : 'rotateZ(180deg)';
    setTimeout(function() {
        imagenFlechaUsuario.style.transition = '';
    }, 300);
    });



    fetch("http://127.0.0.1:8000/servidores/", {
        method: "GET",
        credentials: "include" // Configura para incluir automáticamente las cookies si es necesario
    })
    .then(response => response.json()) // Si esperas una respuesta JSON
    .then(data => {
        // Acceder a los datos JSON y mostrarlos en el HTML
        const resultadosDiv = document.querySelector(".server-icon");
        console.log(data)
        // Iterar sobre el arreglo de objetos
        data[0].forEach(servidor => {
            // Crear elementos HTML para mostrar la información del servidor

            const imageElement = document.createElement("img");
            imageElement.className = "server-icon";
            imageElement.src = servidor.imagen;
            
            const anchorElement = document.createElement("a");
            anchorElement.href = "#";

            anchorElement.addEventListener("click", function(event) {
                event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace

                // Llamar a la función para obtener datos del canal
                obtenerDatosDelCanal(servidor)
                    .then(canales => {
                        // Procesar la respuesta y mostrar los datos en tu interfaz de usuario
                        // const miDiv = document.querySelector(".lista-canales");
                        // miDiv.innerHTML = "";
                        // canales[0].forEach(function(canal) {
                        //     const pElement = document.createElement("p");
                        //     pElement.textContent = canal.nombre
                        //     miDiv.appendChild(pElement);
                    //});
                        console.log(canales)
                        // Puedes mostrar los datos en la interfaz de usuario aquí,
                        // ya sea reemplazando elementos existentes o creando nuevos.
                    });
            // Puedes seguir creando elementos para otros datos del servidor y categoría aquí
        });
            // Agregar los elementos al elemento "resultados" en el HTML
            anchorElement.appendChild(imageElement);
            resultadosDiv.appendChild(anchorElement);
        });
    })    
    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });
});



function obtenerDatosDelCanal(servidor) {
    // Realizar una solicitud GET a la URL deseada
    return fetch("http://127.0.0.1:8000/canales/" + servidor.token, {
        method: "GET",
        credentials: "include" // Configura para incluir automáticamente las cookies si es necesario
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error en la solicitud");
        }
        return response.json(); // Si esperas una respuesta JSON
    })
    .then(data => {
        const tituloServidor = document.querySelector(".titulo-servidor");
        tituloServidor.textContent = servidor.nombre;
        const miDiv = document.querySelector(".lista-canales");
        miDiv.innerHTML = "";
        data[0].forEach(function(canal) {
            const pElement = document.createElement("p");
            pElement.textContent = canal.nombre;
            miDiv.appendChild(pElement);
        });
        return data;
    })
    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });
}