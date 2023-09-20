

function obtenerMensajesDelCanal(id_canal) {
    // Realizar una solicitud GET a la URL deseada
    const h4h3Elements = document.querySelectorAll(".canales-clickleables");
    h4h3Elements.forEach(function(elementos) {
        elementos.addEventListener("click", function(event) {
            h4h3Elements.forEach(function(el) {
                el.classList.remove("clicked");
            });
            this.classList.add("clicked");
        });
    });

    fetch("http://127.0.0.1:8000/mensajes/" + id_canal, {
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

        const seccionDerecha = document.querySelector(".servidor-search");
        seccionDerecha.innerHTML = "";
        const divTituloCanal = document.createElement("div");
        divTituloCanal.className = 'titulo-canal';
        const seccionMensajes = document.createElement("div");
        seccionMensajes.className = 'seccion-mensajes';
        

        
        data[0].forEach(function(mensaje) {
            console.log(mensaje)
            const pMensaje = document.createElement("p");
            pMensaje.textContent = mensaje.mensaje;
            pMensaje.className = "p-mensajes";
            seccionMensajes.appendChild(pMensaje);
        });
        seccionDerecha.appendChild(divTituloCanal);
        seccionDerecha.appendChild(seccionMensajes);
        return data;
    })
    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });
}



export { obtenerMensajesDelCanal }