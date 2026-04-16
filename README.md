<div align="center">
  <h1>🌴 Lakbay API Backend</h1>
  <p>The core powerhouse driving authentication and data management for the Lakbay Vue.js application.</p>

  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
</div>

---

## 📖 Overview

This repository contains the backend architecture for **Lakbay**, built primarily with **FastAPI**. It handles user provisioning, data validation, password hashing (via `bcrypt`), and secure API token generation using JSON Web Tokens (JWT).

## 🚀 Getting Started

To get the backend instance running locally, follow these steps:

### 1. Set Up the Environment
Make sure you have an active Virtual Environment (`.venv`). If you haven't activated it, run:
```bash
# Windows
.venv\Scripts\activate
```

### 2. Install Dependencies
Install all required security, database, and system packages listed in the requirements file:
```bash
pip install -r requirements.txt
```

### 3. Run the Server
Using the FastAPI CLI, spin up the auto-reloading development server:
```bash
fastapi dev app/main.py
```
> The server will start locally at `http://127.0.0.1:8000`. You can also visit `http://127.0.0.1:8000/docs` to test endpoints visually using the automatic Swagger UI dashboard!

---

## 🔗 Connecting with Vue.js

The backend is already configured with CORS to allow connections from Vite's default dev environment (`http://localhost:5173`). 

### What to Install in Vue.js
To easily consume these APIs in your `lakbay-web` frontend, it is highly recommended to use **Axios**. In your Vue web directory, install it via:
```bash
npm install axios
```

### Example Usage
```javascript
import axios from 'axios';

// Example: Logging a user in
const loginUser = async (email, password) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/auth/login', {
      email: email,
      password: password
    });
    
    // Save the returned access_token to localStorage or Vuex/Pinia!
    const token = response.data.access_token;
    console.log("Logged in!", token);
  } catch (error) {
    console.error("Login failed:", error);
  }
};
```

---

## 🌐 API Reference

Below are the foundational routes currently available for consumption by your Vue frontend.

| Method | Endpoint | Description | Payload Body (JSON) | Expected Response |
| :--- | :--- | :--- | :--- | :--- |
| **`POST`** | `/api/auth/register` | Registers a new user account into the SQLite Database. | `{ "email": "...", "password": "..." }` | Returns the created user object (id, email, etc). |
| **`POST`** | `/api/auth/login` | Authenticates an existing user and retrieves a stateless access token. | `{ "email": "...", "password": "..." }` | `{ "access_token": "...", "token_type": "bearer" }` |

> *Note: Both routes require the password payload to be completely valid and at least 8 characters long.*
