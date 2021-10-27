import unittest

from lib.module1 import fib_generator
from lib.module2 import factorial


class TestMath(unittest.TestCase):

    def test_factorial_valid_input(self):
        expected = 6
        actual = factorial(3)
        self.assertEqual(expected, actual)

    def test_factorial_0_input(self):
        expected = 0
        actual = factorial(0)
        self.assertEqual(expected, actual)

    def test_factorial_invalid_input(self):
        self.assertRaises(ValueError, factorial, 100)

    def test_fib_generator(self):
        expected = [0, 1, 1]
        actual = list(fib_generator(3))
        self.assertListEqual(expected, actual)
