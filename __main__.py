from lib.module1 import fib_generator
from lib.module2 import factorial


def main():
    g = fib_generator()
    for i, fib_i in enumerate(g):
        print(f"Fib. number {i} - {fib_i}")

    print(f"Factorial: {factorial(12)}")


if __name__ == "__main__":
    main()
