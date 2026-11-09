import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add_numbers, subtract_numbers, multiply_numbers


class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 2), 3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 6), 24)

if __name__ == "__main__":
    unittest.main()