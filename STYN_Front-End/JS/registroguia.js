// ================================
// JS/registroguia.js
// Manejo del registro de Guía Turístico
// ================================

async function registrarGuia(event) {
  event.preventDefault(); // Evita refresh del form

  // Obtener token del usuario logueado
  const token = localStorage.getItem("token");
  if (!token) {
    alert("Debes iniciar sesión para registrarte como guía.");
    window.location.href = "login.html";
    return;
  }

  // Formulario y FormData
  const form = document.getElementById("form-registro-guia");
  const formData = new FormData(form);

  try {
    const res = await fetch("http://127.0.0.1:8000/Usuarios/UsuarioGuia/registro/", {
      method: "POST",
      headers: {
        "Authorization": "Token " + token
        // NO necesitamos Content-Type: multipart se asigna automáticamente
      },
      body: formData
    });

    const data = await res.json(); // Obtener respuesta JSON
    console.log("Respuesta del back-end:", data);

    if (res.ok) {
      alert("¡Registro de guía completado con éxito!");
      window.location.href = "../HTML/dashboard.html";
    } else {
      alert("Error en el registro: " + JSON.stringify(data));
    }

  } catch (error) {
    console.error(error);
    alert("Error inesperado al registrar guía.");
  }
}

// Autocompletar datos visibles del usuario logueado (opcional)
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form-registro-guia");
  if (!form) return;

  // Evento de submit
  form.addEventListener("submit", registrarGuia);

  // Mostrar el username o email en un campo de solo lectura si quieres
  const user = JSON.parse(localStorage.getItem("user"));
  if (user) {
    const usernameInput = document.getElementById("username");
    if (usernameInput) {
      usernameInput.value = user.username; // mostrar el username
      usernameInput.readOnly = true;       // opcional, no editable
    }
  }
});
