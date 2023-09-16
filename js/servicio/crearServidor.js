function crearFormulario(campos, titulo, onSubmitCallback) {
    var form = document.createElement('form');
    form.className = 'form-login-container';
    form.enstype = 'multipart/form-data'

    var formTitle = document.createElement('h2');
    formTitle.className = 'text-1';
    formTitle.textContent = titulo.toUpperCase();
    form.appendChild(formTitle);

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
                var input = form.querySelector('[name="' + campo.name.toLowerCase().replace(/\s+/g, '') + '"]');
                formData[campo.name] = input.value;
            });
            onSubmitCallback(formData); // Ahora formData es un objeto con los valores de los inputs
        }
    });

    form.appendChild(submitButton);

    return form;
}

// Exportar la función crearFormulario para que esté disponible en otros archivos
export { crearFormulario };
