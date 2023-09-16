import { crearFormulario } from "./servicio/crearServidor.js";
import { performFetch } from "./servicio/requestTemplate.js";
document.addEventListener("DOMContentLoaded", function () {
    
    // Realizar una solicitud GET al servidor cuando la página se carga

    var tituloServidor = document.querySelector(".contenedor-titulo");
    var popupServidor = document.querySelector(".popup-servidor");
    var imagenFlecha = document.querySelector(".flecha");
    var popupVisible = false;

    //SECCION DEL BOTON AGREGAR SERVIDOR
    const addservidor = document.querySelector(".add-icon");
    const ventanaEmergente = document.querySelector('#ventanaEmergente');

    // Agregar el botón de cierre "X" en la esquina superior derecha
    const cerrarBtn = document.createElement('span');
    cerrarBtn.id = 'cerrarBtn';
    cerrarBtn.textContent = '×';
    cerrarBtn.addEventListener('click', () => {
        // Ocultar la ventana emergente cuando se hace clic en el botón de cierre
        ventanaEmergente.style.display = 'none';
    });

    //SECCION DEL BOTON AGREGAR SERVIDOR
    addservidor.addEventListener("click", () => {
        console.log("Add servidor");
        let formulario = crearFormulario(
            [
                { name: "nombre", type: "text" },
                { name: "descripcion", type: "text" },
                { name: "imagen", type: "file" },
                { name: "privado", type: "checkbox"} // Usar 'file' para campos de tipo archivo (imagen en este caso)
            ],
            "CREAR SERVIDOR",
            (form) => {
                var formData = new FormData();
                formData.append("id_categoria", 1);
                formData.append("nombre", form.nombre);
                formData.append("descripcion", form.descripcion);
                formData.append("privado", form.privado === "on" ? "true" : "false");
                formData.append("imagen", form.imagen);
            
                // Define the data for the Fetch request
                const fetchData = {
                    url: 'http://127.0.0.1:8000/servidores/crear', // URL of the API where you want to send the form
                    method: 'POST', // POST method to send data
                    headers: {
                        // Configure Content-Type header for form data with a file
                        'Accept': 'application/json',
                    },
                    body: formData // Use the FormData object as the request body
                };
            
                // Call the performFetch function with the fetchData object
                performFetch(fetchData)
                    .then(responseData => {
                        console.log(responseData); // Handle the response data here
                    })
                    .catch(error => {
                        console.error('Error:', error); // Handle errors here
                    });
            }
            
            
        );
        
        
        // Agregar el formulario al contenedor de la ventana emergente
        ventanaEmergente.innerHTML = '';
        
        // Agregar el botón de cierre en la esquina superior derecha
        ventanaEmergente.appendChild(cerrarBtn);
        
        ventanaEmergente.appendChild(formulario);
        
        // Mostrar la ventana emergente
        ventanaEmergente.style.display = 'block';
    });

    // Para ocultar la ventana emergente en otro evento (por ejemplo, al hacer clic en el botón de cierre principal)
    function ocultarVentanaEmergente() {
        ventanaEmergente.style.display = 'none';
    }
    //FIN

    
    
    

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
            pElement.textContent = "#"+canal.nombre;
            miDiv.appendChild(pElement);
        });
        return data;
    })
    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });
}




 