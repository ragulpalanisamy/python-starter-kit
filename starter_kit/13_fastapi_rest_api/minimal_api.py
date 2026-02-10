"""
FastAPI Basics - A Minimal Web API

This script demonstrates a single-file FastAPI application.
For the full production-ready structure, see the 'fastapi-starter/' directory.
"""

try:
    from fastapi import FastAPI
    import uvicorn
except ImportError:
    print("FastAPI or Uvicorn not installed. Install with: pip install fastapi uvicorn")
    exit(1)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from the Starter Kit!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "status": "found"}

if __name__ == "__main__":
    print("Starting minimal FastAPI app...")
    print("Open http://127.0.0.1:8000 in your browser.")
    uvicorn.run(app, host="127.0.0.1", port=8000)
