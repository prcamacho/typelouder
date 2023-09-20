function cargarBienvenida(descripcion){
    const seccionDerecha = document.querySelector(".servidor-search");
    seccionDerecha.innerHTML = "";
    const divTituloCanal = document.createElement("div");
    divTituloCanal.className = 'titulo-canal';
    const seccionMensajes = document.createElement("div");
    seccionMensajes.className = 'seccion-mensajes';
    const mensajeBienvenida = document.createElement('p');
    mensajeBienvenida.textContent = descripcion;
    seccionMensajes.appendChild(mensajeBienvenida);
    seccionDerecha.appendChild(divTituloCanal);
    seccionDerecha.appendChild(seccionMensajes);
}

export { cargarBienvenida }