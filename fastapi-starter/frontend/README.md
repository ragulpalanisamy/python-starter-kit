# 💻 React + TypeScript Frontend

> **Modern Frontend with React, Vite, and Tailwind CSS**

The user-facing side of the FastAPI starter project, built for speed and type safety.

[![React](https://img.shields.io/badge/React-18-blue.svg)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue.svg)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-6-purple.svg)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38bdf8.svg)](https://tailwindcss.com/)

---

## ✨ Features

✅ **Fast Development** - Vite for near-instant HMR (Hot Module Replacement)  
✅ **Type Safety** - Fully typed components and API interactions  
✅ **Responsive Design** - Built with Tailwind CSS  
✅ **State Management** - Redux Toolkit (RTK Query) for API integration  
✅ **UI Components** - Modern, accessible components (Radix UI / Shadcn UI pattern)  
✅ **Icons** - Beautiful icons from Lucide React

---

## 📁 Project Structure

```
frontend/
├── src/
│   ├── assets/       # Static assets (images, fonts)
│   ├── components/   # Reusable UI components
│   ├── layout/       # Page layouts
│   ├── pages/        # Application views/screens
│   ├── services/     # API services and Redux slices
│   ├── styles/       # Global CSS and Tailwind directives
│   └── App.tsx       # Root component and Routing
├── index.html        # Entry point
└── package.json      # Node dependencies
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment

Create a `.env` file in the `frontend` root:

```env
VITE_API_URL=http://localhost:8000
```

### 3. Run Development Server

```bash
npm run dev
```

The app will be available at: **http://localhost:5173**

---

## 🧪 Common Commands

```bash
npm install        # Install packages
npm run dev        # Start development server
npm run build      # Build for production
npm run lint       # Run ESLint
npm run preview    # Preview production build locally
```

---

## 💡 Frontend-Backend Integration

This frontend is designed to interact with the FastAPI backend. It uses **RTK Query** for efficient data fetching, caching, and state management.

See `src/services/apiSlice.ts` for the base configuration.

---

## 👤 Author

**Ragul P** - [@ragulpalanisamy](https://github.com/ragulpalanisamy)

---

_Happy Coding! 🚀_
