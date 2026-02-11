# 📦 Environment & Package Management

In Node/MERN, you have `npm` and `node_modules`. In Python, we use **Virtual Environments** and packages from **PyPI**.

## 1. node_modules vs .venv

- **`node_modules`**: Usually sits in your project root. Can be massive.
- **`.venv` (Virtual Environment)**: Python isolated environment. It keeps your project's dependencies separate from the system's Python.

## 2. Meet `uv`: The modern standard

`uv` is an extremely fast Python package manager (written in Rust) that replaces `pip`, `pip-tools`, and `virtualenv`.

### Comparison of Commands

| Action              | npm                  | uv                      |
| ------------------- | -------------------- | ----------------------- |
| **Install project** | `npm install`        | `uv sync`               |
| **Add a package**   | `npm install lodash` | `uv add pandas`         |
| **Run a script**    | `npm run start`      | `uv run python main.py` |
| **Init project**    | `npm init`           | `uv init`               |

## 3. pyproject.toml

This is your `package.json`. It looks like this:

```toml
[project]
name = "my-python-app"
version = "0.1.0"
dependencies = [
    "fastapi>=0.100.0",
    "uvicorn>=0.22.0",
]
```

## ⚡ Pro Tip for MERN Switchers

Always run your Python code through `uv run`. It ensures you're using the correct environment, exactly like `npm run` or `npx`.

---

[⬅️ Back to Learning Path](../index.md)
