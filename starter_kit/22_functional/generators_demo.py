# Generators Demo

def fibonacci_generator(limit):
    """A generator for Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def main():
    print("Fibonacci numbers under 100:")
    fib_gen = fibonacci_generator(100)
    
    for num in fib_gen:
        print(num, end=" ")
    print()

    # Another generator example
    squares = (x*x for x in range(5)) # Generator expression
    print("Squares using generator expression:")
    for s in squares:
        print(s, end=" ")
    print()

if __name__ == "__main__":
    main()
