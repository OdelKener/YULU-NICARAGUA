// URL base de tu API
const BASE_URL = "http://127.0.0.1:8000/";

// Función genérica POST
async function post(endpoint, data) {
  const url = BASE_URL + endpoint; // concatena base + endpoint
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  // Manejo de errores HTTP
  if (!res.ok) {
    const errorData = await res.json().catch(() => ({}));
    throw new Error(`HTTP ${res.status}: ${JSON.stringify(errorData)}`);
  }

  return await res.json();
}

// --- Registro de usuario ---
async function registerUser(formData) {
  try {
    // endpoint relativo al BASE_URL, siempre con slash final
    const data = await post("Usuarios/Auth/registro/", formData);

    if (data.user) {
      alert(data.mensaje || "Usuario registrado correctamente");
      window.location.href = "login.html";
    } else {
      throw new Error("Error en registro: " + JSON.stringify(data));
    }
  } catch (err) {
    alert(err);
  }
}

// --- Login de usuario ---
// JS/auth.js

async function loginUser(event) {
  event.preventDefault();

  const form = document.getElementById("form-login");
  const email = form.email.value;
  const password = form.password.value;

  try {
    const res = await fetch("http://127.0.0.1:8000/Usuarios/Auth/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (!res.ok) throw new Error("Login fallido: " + JSON.stringify(data));

    // Guardar token y datos del usuario
    localStorage.setItem("token", data.token);
    localStorage.setItem("user", JSON.stringify(data.user));
    localStorage.setItem("perfil_turistico", JSON.stringify(data.perfil_turistico));

    // Redirigir al dashboard
    window.location.href = "../HTML/dashboardprincipal.html";

  } catch (err) {
    alert(err);
  }
}

// Evento al cargar la página
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form-login");
  if (form) form.addEventListener("submit", loginUser);
});

// --- Formulario de login ---
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("form-login");
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = loginForm.email.value;
      const password = loginForm.password.value;
      await loginUser(email, password);
    });
  }

  const registroForm = document.getElementById("form-registro-guia");
  if (registroForm) {
    registroForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      // Creamos formData desde inputs del formulario
      const formDataObj = {};
      new FormData(registroForm).forEach((value, key) => {
        formDataObj[key] = value;
      });

      await registerUser(formDataObj);
    });
  }
});
