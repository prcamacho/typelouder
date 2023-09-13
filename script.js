function cambiarContenido(idContenido) {
    // Ocultar todos los elementos de contenido
    const elementosContenido = document.querySelectorAll('.content div');
    elementosContenido.forEach(elemento => {
        elemento.style.display = 'none';
    });

    // Mostrar el elemento de contenido seleccionado
    const contenidoSeleccionado = document.getElementById(idContenido);
    contenidoSeleccionado.style.display = 'block';
}
