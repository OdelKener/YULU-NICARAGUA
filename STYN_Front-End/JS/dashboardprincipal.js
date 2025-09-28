document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token");
  if (!token) {
    alert("Debes iniciar sesión.");
    window.location.href = "login.html";
    return;
  }

  // Botón registrar guía
  const registrarGuiaBtn = document.getElementById("registrar-guia");
  registrarGuiaBtn.addEventListener("click", () => {
    window.location.href = "../HTML/registroguia.html";
  });

  // Botón reservas
  const reservasBtn = document.getElementById("reservas");
  reservasBtn.addEventListener("click", () => {
    window.location.href = "../HTML/reservas.html"; // tu archivo de reservas
  });
});



