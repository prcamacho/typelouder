document.addEventListener("DOMContentLoaded", function () {
    // Realizar una solicitud GET al servidor cuando la página se carga

    var tituloServidor = document.querySelector(".contenedor-titulo");
    var popupServidor = document.querySelector(".popup-servidor");

    tituloServidor.addEventListener('click', function() {
        if (popupServidor.style.display== 'none'){
            popupServidor.style.display = 'block';
        }else{
            popupServidor.style.display = 'none';
        }
    });

    





    fetch("http://127.0.0.1:8000/servidores/", {
        method: "GET",
        credentials: "include" // Configura para incluir automáticamente las cookies si es necesario
    })
    .then(response => response.json()) // Si esperas una respuesta JSON
    .then(data => {
        // Acceder a los datos JSON y mostrarlos en el HTML
        const resultadosDiv = document.querySelectorAll(".server-icon");
        const resultadoTitulo =

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
            resultadosDiv[1].appendChild(anchorElement);
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
        tituloServidor.textContent = servidor.nombre+"adasdasdasdasdasdasdasd";
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