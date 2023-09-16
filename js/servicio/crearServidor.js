function crearFormulario(campos, titulo, onSubmitCallback) {
    var form = document.createElement('form');
    form.className = 'form-login-container';
    form.enctype = 'multipart/form-data';

    var formTitle = document.createElement('h2');
    formTitle.className = 'text-1';
    formTitle.textContent = titulo.toUpperCase();
    form.appendChild(formTitle);

    var fileInputs = {}; // Objeto para almacenar los campos de tipo 'file'

    campos.forEach(function (campo) {
        var label = document.createElement('label');
        label.className = 'label-form';
        label.textContent = campo.name.toUpperCase();

        var input = document.createElement('input');
        input.className = 'input-form';
        input.type = campo.type || 'text';
        input.name = campo.name.toLowerCase().replace(/\s+/g, '');

        form.appendChild(label);
        form.appendChild(input);

        if (campo.type === 'file') {
            // Si el campo es de tipo 'file', guardar una referencia al input en el objeto fileInputs
            fileInputs[campo.name] = input;
        }
    });

    var submitButton = document.createElement('button');
    submitButton.className = 'boton-login';
    submitButton.type = 'submit';
    submitButton.textContent = 'ACEPTAR';

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        if (typeof onSubmitCallback === 'function') {
            var formData = {};
            campos.forEach(function (campo) {
                if (campo.type === 'file') {
                    // Si el campo es de tipo 'file', guardar el archivo en el objeto formData
                    formData[campo.name] = fileInputs[campo.name].files[0];
                } else {
                    var input = form.querySelector('[name="' + campo.name.toLowerCase().replace(/\s+/g, '') + '"]');
                    formData[campo.name] = input.value;
                }
            });
            onSubmitCallback(formData); // Ahora formData es un objeto con los valores de los inputs, incluyendo archivos
        }
    });

    form.appendChild(submitButton);

    return form;
}

// Exportar la función crearFormulario para que esté disponible en otros archivos
export { crearFormulario };
