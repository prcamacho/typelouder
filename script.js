document.addEventListener('DOMContentLoaded', function() {
    var mostrarBtn = document.getElementById('mostrarBtn');
    var ventanaEmergente = document.getElementById('ventanaEmergente');
    var cerrarBtn = document.getElementById('cerrarBtn');

    mostrarBtn.addEventListener('click', function() {
        ventanaEmergente.style.display = 'block';
    });

    cerrarBtn.addEventListener('click', function() {
        ventanaEmergente.style.display = 'none';
    });
});
