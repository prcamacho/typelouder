
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".form-login");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            body: formData,
            credentials: "include" // Configurar para incluir automáticamente las cookies
        })
        .then(response => {
                window.location.href = "../page/main.html";

        })
        .catch(error => {
            // Manejar el error en caso de que ocurra
            console.error("Error:", error);
        });
    });
});
