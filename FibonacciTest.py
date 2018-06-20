"""
TESTS
"""

import unittest

from Fibonacci import Fibonacci

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.fib = Fibonacci()

    def test_should_fibonacci__raise_exception_due_to_negative_number_of_months(self):
        with self.assertRaises(Exception):
            self.fib.compute(-1, 1)

    def test_should_fibonacci__raise_exception_due_to_negative_number_of_pairs(self):
        with self.assertRaises(Exception):
            self.fib.compute(1, -1)

    def test_should_fibonacci_zero_return_zero(self):
        self.assertEqual(0, self.fib.compute(0, 1))

    def test_should_fibonacci_one_return_one(self):
        self.assertEqual(1, self.fib.compute(1, 1))

    def test_should_fibonacci_of_two_return_one(self):
        self.assertEqual(1, self.fib.compute(2, 1))

    def test_should_fibonacci_of_three_return_two(self):
        self.assertEqual(2, self.fib.compute(3, 1))

    def test_should_fibonacci_of_four_return_three(self):
        self.assertEqual(3, self.fib.compute(4, 1))

    def test_should_fibonacci_ROSALIND(self):
        self.assertEqual(19, self.fib.compute(5, 3))

    def tearDown(self):
        print("Test probado con éxito")


if __name__=='__main__':
    unittest.main()
