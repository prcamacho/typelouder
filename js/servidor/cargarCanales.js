import { obtenerMensajesDelCanal } from "./cargarMensajes.js";

function obtenerCanales(servidor_token) {
    // Realizar una solicitud GET a la URL deseada
    return fetch("http://127.0.0.1:8000/canales/" + servidor_token, {
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
        const miDiv = document.querySelector(".canales");
        miDiv.innerHTML = "";
        miDiv.classList.add("contenedor-canales"); 
        data[0].forEach(function(canal) {
            const h4Element = document.createElement("h4");
            h4Element.textContent = "# "+canal.nombre;
            h4Element.className = "canales-clickleables";
            h4Element.id = 'canal'+canal.id;
            miDiv.appendChild(h4Element);
        });
        miDiv.addEventListener("click", function(event) {
            if (event.target.classList.contains("canales-clickleables")) {
                // Se hizo clic en un elemento h4 con la clase "canales-clickleables"
                const clickedH4 = event.target;
                const id = clickedH4.id;
                const parteNumerica = id.match(/\d+/);
                const id_canal = parseInt(parteNumerica[0], 10);
        
                obtenerMensajesDelCanal(id_canal);
                
                // Realiza la acción deseada con el ID del canal
        
                // Elimina la clase "clicked" de todos los elementos h4 y agrega la clase "clicked" al clicado
                const h4Elements = miDiv.querySelectorAll(".canales-clickleables");
                h4Elements.forEach(function(el) {
                    el.classList.remove("clicked");
                });
                clickedH4.classList.add("clicked");
            }
        });
    })
    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });
}

export{ obtenerCanales }