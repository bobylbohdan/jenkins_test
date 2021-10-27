def factorial(n: int) -> int:
    if n > 12 or n < 0:
        raise ValueError(f"n == {n} is invalid. n should be in range [0...12]")

    if n == 0:
        return 0

    f = 1
    for i in range(2, n+1):
        f *= i

    return f
