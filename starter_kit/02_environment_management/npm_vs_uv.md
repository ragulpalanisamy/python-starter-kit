# npm vs uv: Package Management

This guide explains the mapping between common Node.js commands and Python's `uv` commands.

## 1. Project Initialization

- **MERN:** `npm init -y`
- **Python:** `uv init`

## 2. Installing Dependencies

- **MERN:** `npm install express`
- **Python:** `uv add fastapi`

## 3. Dev Dependencies

- **MERN:** `npm install -D jest`
- **Python:** `uv add --dev pytest`

## 4. Running the App

- **MERN:** `node index.js` or `npm start`
- **Python:** `uv run python main.py`

## 5. Cleaning up

- **MERN:** `rm -rf node_modules`
- **Python:** `rm -rf .venv`

---

_Note: Always use `uv run` to ensure you are in the project's isolated environment._
