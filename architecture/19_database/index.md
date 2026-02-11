# Database Connectivity

Connecting Python to a database securely.

## 1. Using `.env` for Secrets

Never hardcode passwords! Use `python-dotenv`.

```bash
pip install python-dotenv
```

**.env file:**

```
DB_PASSWORD=my_secure_password
```

**python code:**

```python
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("DB_PASSWORD")
```

## 2. PostgreSQL Example (psycopg2)

```python
import psycopg2

conn = psycopg2.connect(
    dbname="mydb",
    user="myuser",
    password=os.getenv("DB_PASSWORD"),
    host="localhost"
)
```

---

[⬅️ Back to Learning Path](../index.md)
