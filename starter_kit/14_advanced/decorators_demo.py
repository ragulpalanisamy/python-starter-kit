import time

# Decorators are like "Middleware" for functions in Python.

def timer_decorator(func):
    """A decorator that measures the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f}s to run.")
        return result
    return wrapper

@timer_decorator
def heavy_computation():
    """Simulates a task that takes time."""
    print("Computing...")
    time.sleep(1)
    print("Done!")

def main():
    print("--- Decorators Demo ---")
    heavy_computation()

if __name__ == "__main__":
    main()
