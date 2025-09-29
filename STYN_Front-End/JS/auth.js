// URL base de tu API
const BASE_URL = "http://127.0.0.1:8000/";

// Función genérica POST
async function post(endpoint, data) {
  const url = BASE_URL + endpoint;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({}));
    throw new Error(`HTTP ${res.status}: ${JSON.stringify(errorData)}`);
  }

  return await res.json();
}

// --- Registro de usuario ---
async function registerUser(formData) {
  try {
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

// --- Login de usuario CORREGIDO ---
async function loginUser(email, password) {
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

// --- Solo UN event listener para el login ---
document.addEventListener("DOMContentLoaded", () => {
  // Login form
  const loginForm = document.getElementById("loginForm");
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      await loginUser(email, password);
    });
  }

  // Registro form (si lo necesitas)
  const registroForm = document.getElementById("form-registro-guia");
  if (registroForm) {
    registroForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      const formDataObj = {};
      new FormData(registroForm).forEach((value, key) => {
        formDataObj[key] = value;
      });

      await registerUser(formDataObj);
    });
  }
});