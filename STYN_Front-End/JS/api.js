// JS/api.js
const API_URL = "http://127.0.0.1:8000/";

// POST genérico
async function post(endpoint, data, useToken=false) {
  const headers = { "Content-Type": "application/json" };
  if (useToken) {
    const token = localStorage.getItem("token");
    if (token) headers["Authorization"] = `Token ${token}`;
  }
  const res = await fetch(API_URL + endpoint, {
    method: "POST",
    headers,
    body: JSON.stringify(data)
  });
  return res.json();
}

// GET genérico
async function get(endpoint, useToken=false) {
  const headers = {};
  if (useToken) {
    const token = localStorage.getItem("token");
    if (token) headers["Authorization"] = `Token ${token}`;
  }
  const res = await fetch(API_URL + endpoint, { headers });
  return res.json();
}

