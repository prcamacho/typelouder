document.addEventListener('DOMContentLoaded', function() {
    var ventanaEmergente = document.getElementById('ventanaEmergente');

    // Función para crear dinámicamente un formulario con un título personalizado
    function crearFormulario(labels, titulo) {
        var contenido = document.createElement('div');
        contenido.id = 'contenido';

        var form = document.createElement('form');
        form.className = 'form-login';

        // Agregar el título personalizado al formulario en mayúsculas
        var formTitle = document.createElement('h2');
        formTitle.className = 'text-1';
        formTitle.textContent = titulo.toUpperCase();
        form.appendChild(formTitle);

        labels.forEach(function(labelText) {
            var label = document.createElement('label');
            label.className = 'label-form';
            label.textContent = labelText.toUpperCase(); // Convertir etiqueta a mayúsculas

            var input = document.createElement('input');
            input.className = 'input-form';
            input.type = 'text'; // Puedes ajustar el tipo de entrada según tus necesidades
            input.name = labelText.toLowerCase().replace(/\s+/g, ''); // Genera un nombre único para cada campo

            form.appendChild(label);
            form.appendChild(input);
        });

        var submitButton = document.createElement('button');
        submitButton.className = 'boton-login';
        submitButton.type = 'submit';
        submitButton.textContent = 'ACEPTAR';

        form.appendChild(submitButton);
        contenido.appendChild(form);

        // Crear el botón de cierre dinámicamente
        var cerrarBtn = document.createElement('span');
        cerrarBtn.id = 'cerrarBtn';
        cerrarBtn.textContent = '×';
        contenido.appendChild(cerrarBtn);

        return contenido;
    }

    // Crear el botón "Mostrar Ventana Emergente" dinámicamente
    var mostrarBtn = document.createElement('button');
    mostrarBtn.id = 'mostrarBtn';
    mostrarBtn.textContent = 'Mostrar Ventana Emergente';
    document.body.appendChild(mostrarBtn);

    mostrarBtn.addEventListener('click', function() {
        // Ejemplo de lista de etiquetas con 4 elementos
        var labels = ['Nombre'];

        // Puedes pasar un título personalizado como argumento
        var tituloFormulario = 'CREAR SERVIDOR';

        var contenido = crearFormulario(labels, tituloFormulario);

        ventanaEmergente.innerHTML = ''; // Borra el contenido anterior
        ventanaEmergente.appendChild(contenido);

        ventanaEmergente.style.display = 'block';
    });

    // Agregar el evento de cierre dinámicamente
    document.body.addEventListener('click', function(event) {
        if (event.target.id === 'cerrarBtn') {
            ventanaEmergente.style.display = 'none';
        }
    });
});
