import { crearFormulario } from "./servidor/crearServidor.js";
import { performFetch } from "./servidor/requestTemplate.js";
import { obtenerCanales } from "./servidor/cargarCanales.js";
import { cargarBienvenida } from "./servidor/cargarBienvenida.js";

document.addEventListener("DOMContentLoaded", function () {

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
                formData.append("privado", form.privado === "off" ? "true" : "false");
                formData.append("imagen", form.imagen);
            
                // Define the data for the Fetch request
                const fetchData = {
                    url: 'http://127.0.0.1:8000/servidores/crear', // URL of the API where you want to send the form
                    method: 'POST', // POST method to send data
                    headers: {
                        // Configure Content-Type header for form data with a file
                    },
                    body: formData // Use the FormData object as the request body
                };
            
                // Call the performFetch function with the fetchData object
                performFetch(fetchData)
                    .then(responseData => {
                        ventanaEmergente.style.display = 'none';
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
    popupServidor.style.transform = popupVisible ? 'translateY(0%)' : 'translateY(100%)';
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
            anchorElement.id=servidor.token;
            anchorElement.href = "#";

            anchorElement.addEventListener("click", function(event) {
                event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
                const tituloServidor = document.querySelector(".titulo-servidor");
                tituloServidor.textContent = servidor.nombre;

                    // const seccionDerecha = document.querySelector(".servidor-search");
                    // seccionDerecha.innerHTML = "";
                    // const divTituloCanal = document.createElement("div");
                    // divTituloCanal.className = 'titulo-canal';
                    // const seccionMensajes = document.createElement("div");
                    // seccionMensajes.className = 'seccion-mensajes';
                    // const mensajeBienvenida = document.createElement('p');
                    // mensajeBienvenida.textContent = servidor.descripcion;
                    // seccionMensajes.appendChild(mensajeBienvenida);
                    // seccionDerecha.appendChild(divTituloCanal);
                    // seccionDerecha.appendChild(seccionMensajes);
                    cargarBienvenida(servidor.descripcion);
                    obtenerCanales(this.id);
                
        });
            // Agregar los elementos al elemento "resultados" en el HTML
            anchorElement.appendChild(imageElement);
            resultadosDiv.appendChild(anchorElement);
        });

        // const canalesh4 = document.querySelectorAll(".canales-clickleables");
        // console.log(JSON.stringify(canalesh4));
        // canalesh4.forEach(function(canal) {
        //     hola.addEventListener("click", function(event) {
        //         event.preventDefault();
                
        //         var id = this.id
        //         console.log(id)
        //         var parteNumerica = id.match(/\d+/);
        //         var id_canal = parseInt(parteNumerica[0], 10);
        //         obtenerMensajesDelCanal(id_canal);                 
        //     });           
        //          });
    }) 

    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });   
});








