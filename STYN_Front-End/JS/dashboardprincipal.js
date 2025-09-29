document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token");
  if (!token) {
    alert("Debes iniciar sesión.");
    window.location.href = "login.html";
    return;
  }

  // Botón Catálogos de Aves
  const catalogosBtn = document.getElementById("catalogos");
  if (catalogosBtn) {
    catalogosBtn.addEventListener("click", () => {
      window.location.href = "../HTML/catalogoaves.html";
    });
  }

  // Botón Reservas Naturales
  const reservasNaturalesBtn = document.getElementById("reservas-naturales");
  if (reservasNaturalesBtn) {
    reservasNaturalesBtn.addEventListener("click", () => {
      window.location.href = "../HTML/reservasnaturales.html";
    });
  }

  // Botón Eventos
  const eventosBtn = document.getElementById("eventos");
  if (eventosBtn) {
    eventosBtn.addEventListener("click", () => {
      window.location.href = "../HTML/eventos.html";
    });
  }

  // Botón Sitios Turísticos (CORREGIDO)
  const sitiosTuristicosBtn = document.getElementById("sitios-turisticos");
  if (sitiosTuristicosBtn) {
    sitiosTuristicosBtn.addEventListener("click", () => {
      window.location.href = "../HTML/sitiosturistico.html";
    });
  }

  // Botón Educación
  const educativoBtn = document.getElementById("educativo");
  if (educativoBtn) {
    educativoBtn.addEventListener("click", () => {
      window.location.href = "../HTML/educacion.html";
    });
  }

  // Botón Reservas
  const reservasBtn = document.getElementById("reservas");
  if (reservasBtn) {
    reservasBtn.addEventListener("click", () => {
      window.location.href = "../HTML/reservas.html";
    });
  }

  // Botón Registrar Guía
  const registrarGuiaBtn = document.getElementById("registrar-guia");
  if (registrarGuiaBtn) {
    registrarGuiaBtn.addEventListener("click", () => {
      window.location.href = "../HTML/registroguia.html";
    });
  }


  // Agregar logs para debug
  console.log("Event listeners configurados correctamente");
});



