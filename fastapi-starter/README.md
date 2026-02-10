# 🚀 FastAPI + React Full-stack Starter

> **Modern Full-stack Web Application with FastAPI Backend and React Frontend**

A production-ready full-stack application demonstrating best practices with FastAPI, React, and automated deployment.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://react.dev/)

---

## ✨ Features

✅ **Modern Stack** - FastAPI + UV (Backend) & React + Vite (Frontend)  
✅ **Type Safety** - TypeScript (Frontend) & Python Type Hints (Backend)  
✅ **Clean Architecture** - Modularized backend and component-based frontend  
✅ **Styling** - Tailwind CSS and Lucid Icons  
✅ **State Management** - Redux Toolkit for frontend state and API calls  
✅ **Deployment** - Pre-configured for Render (see `backend/render.yaml`)  
✅ **Auto Documentation** - Swagger UI for API testing

---

## 📁 Project Structure

```
fastapi-starter/
├── backend/             # ⭐ FastAPI REST API
│   ├── app/             # Application logic
│   ├── tests/           # Backend tests
│   └── pyproject.toml   # Python dependencies
├── frontend/            # ⭐ React Frontend
│   ├── src/             # Frontend source code
│   └── package.json     # Node dependencies
└── ARCHITECTURE.md      # Detailed architecture documentation
```

---

## 🚀 Quick Start

### 1. Setup Backend

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

API runs at: **http://localhost:8000**

### 2. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

App runs at: **http://localhost:5173**

---

## 🌐 Deployment (Render)

This project is optimized for deployment on **Render**.

1. **Backend**: Use the provided `backend/render.yaml` for a "Web Service".
2. **Frontend**: Deploy as a "Static Site" pointing to the `dist/` directory after building.

---

## 🎓 Learning Resources

- [Backend README](./backend/README.md) - Deep dive into API structure
- [Frontend README](./frontend/README.md) - Deep dive into UI structure
- [Architecture Guide](./ARCHITECTURE.md) - How the pieces fit together

---

## 👤 Author

**Ragul P** - [@ragulpalanisamy](https://github.com/ragulpalanisamy)

---

_Happy Coding! 🚀_
