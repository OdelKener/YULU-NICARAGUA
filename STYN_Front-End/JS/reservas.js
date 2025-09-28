const API_BASE = "http://127.0.0.1:8000";
const token = localStorage.getItem("token"); // tu JWT del login

document.addEventListener("DOMContentLoaded", () => {
  if (!token) {
    alert("Debes iniciar sesión.");
    window.location.href = "../login.html";
    return;
  }

  // sitios turísticos
 fetch(`${API_BASE}/SitiosTuristicos/sitiosturisticos/`, {
    headers: { Authorization: `Token ${token}` }
})
.then(res => res.json())
.then(data => {
    const selectSitio = document.getElementById("sitio");
    selectSitio.innerHTML = ""; // limpiar opciones
    data.forEach(sitio => {
        const option = document.createElement("option");
        option.value = sitio.id;      // value = id
        option.textContent = sitio.nombre; // mostrar nombre
        selectSitio.appendChild(option);
    });
})
.catch(err => console.error("Error cargando sitios:", err));

  // guías aprobados (ajusta endpoint en tu backend)
 // guías aprobados
fetch(`${API_BASE}/Usuarios/UsuarioGuia/aprobados/`, {
  headers: { Authorization: `Token ${token}` }
})
  .then(res => res.json())
  .then(data => {
    const selectGuia = document.getElementById('guia');
    selectGuia.innerHTML = '';
    data.forEach(guia => {
      const option = document.createElement('option');
      option.value = guia.id;
      option.textContent = `${guia.nombre} ${guia.apellido}`;
      selectGuia.appendChild(option);
    });
  })
  .catch(err => console.error(err));
});

// enviar reserva
document.getElementById("formReserva").addEventListener("submit", e => {
  e.preventDefault();

  const data = {
    guia: document.getElementById("guia").value,
    sitio: document.getElementById("sitio").value,
    fecha_reserva: document.getElementById("fecha_reserva").value,
    hora_inicio: document.getElementById("hora_inicio").value,
    duracion_horas: document.getElementById("duracion_horas").value,
    numero_personas: document.getElementById("numero_personas").value,
    metodo_pago: document.getElementById("metodo_pago").value,
    requisitos_especiales: document.getElementById("requisitos_especiales").value,
    punto_encuentro: document.getElementById("punto_encuentro").value
  };

  fetch(`${API_BASE}/Reservas/reservas/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
    },
    body: JSON.stringify(data)
  })
    .then(async res => {
      const resp = await res.json();
      if (!res.ok) throw resp;
      alert(`Reserva creada. Código de confirmación: ${resp.codigo_confirmacion}`);
    })
    .catch(err => {
      console.error(err);
      alert("Error al crear reserva: " + (err.error || JSON.stringify(err)));
    });
});
