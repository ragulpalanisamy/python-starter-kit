# 🌀 Concurrency: Node vs Python

Both Node.js and modern Python (`FastAPI`) are great for high-performance I/O applications.

## 1. Node.js (The Event Loop)

- Node is single-threaded.
- It uses a non-blocking event loop by default.
- Everything is `async` behind the scenes.

## 2. Python (`asyncio`)

- Python is multi-threaded but restricted by the **GIL** (Global Interpreter Lock) for CPU tasks.
- For I/O tasks (API calls, DB queries), we use `asyncio`.
- You must explicitly mark functions as `async def`.

## 3. Comparison Table

| Feature          | Node.js         | Python (FastAPI)        |
| ---------------- | --------------- | ----------------------- |
| **Model**        | Event Loop      | AsyncIO + GIL           |
| **Keywords**     | `async / await` | `async / await`         |
| **Native Async** | Yes (Core)      | Yes (via `asyncio` lib) |
| **CPU Bound**    | Worker Threads  | `multiprocessing`       |

## 🚀 When to use what?

- **`async/await`**: For web servers, database queries, and API calls.
- **`threading`**: For legacy I/O libraries that don't support `async`.
- **`multiprocessing`**: For heavy computation (Machine Learning, Video processing).

---

[⬅️ Back to Learning Path](../index.md)
