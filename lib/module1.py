def fib_generator(max_fib_numbers: int = 20):
    a, b = 0, 1
    for _ in range(max_fib_numbers):
        yield a
        a, b = b, a + b
