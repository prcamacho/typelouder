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
        data[0].forEach(function(canal) {
            const h4Element = document.createElement("h4");
            h4Element.textContent = "# "+canal.nombre;
            h4Element.className = "canales-clickleables";
            h4Element.id = 'canal'+canal.id;
            miDiv.appendChild(h4Element);
        });
    })
    .catch(error => {
        // Manejar el error en caso de que ocurra
        console.error("Error:", error);
    });
}

export{ obtenerCanales }