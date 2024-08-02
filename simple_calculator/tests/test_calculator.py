import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("1+1"), 2)
        self.assertEqual(calculate("10+5"), 15)
        self.assertEqual(calculate("0+0"), 0)

    def test_subtraction(self):
        self.assertEqual(calculate("5-3"), 2)
        self.assertEqual(calculate("10-15"), -5)
        self.assertEqual(calculate("0-0"), 0)

    def test_multiplication(self):
        self.assertEqual(calculate("2*3"), 6)
        self.assertEqual(calculate("10*0"), 0)
        self.assertEqual(calculate("5*5"), 25)

    def test_division(self):
        self.assertEqual(calculate("6/2"), 3)
        self.assertEqual(calculate("10/5"), 2)
        self.assertEqual(calculate("1/1"), 1)
        
        self.assertEqual(calculate("1/0"), 'float division by zero')

    def test_invalid_operation(self):
        self.assertEqual(calculate("1^1"), "Invalid operation")
        self.assertEqual(calculate("one+one"), "could not convert string to float: 'one'")
        self.assertEqual(calculate("1++1"), "could not convert string to float: ''")
        self.assertEqual(calculate("1--1"), "could not convert string to float: ''")

if __name__ == "__main__":
    unittest.main()