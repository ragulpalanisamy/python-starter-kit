import asyncio
import time

# Comparison between Sync and Async execution in Python.
# Think of this as Node.js callbacks/promises vs blocking JS.

async def fetch_data(id):
    """Simulates an I/O operation (like an API call)."""
    print(f"Starting fetch {id}...")
    await asyncio.sleep(1) # Non-blocking sleep
    print(f"Finished fetch {id}")
    return f"Data {id}"

async def main():
    print("--- Async Comparison Demo ---")
    start = time.time()

    # Running sequentially (blocking)
    print("\nRunning tasks sequentially:")
    await fetch_data(1)
    await fetch_data(2)
    
    mid = time.time()
    print(f"Sequential time: {mid - start:.2f}s")

    # Running concurrently (non-blocking)
    print("\nRunning tasks concurrently (like Promise.all):")
    results = await asyncio.gather(
        fetch_data(3),
        fetch_data(4),
        fetch_data(5)
    )
    
    end = time.time()
    print(f"Concurrent time: {end - mid:.2f}s")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
