import unittest
from lab1 import isMonotonic  

class TestIsMonotonic(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(isMonotonic([1, 2, 3, 4, 5]))

    def test_case_2(self):
        self.assertTrue(isMonotonic([5, 4, 3, 2, 1]))

    def test_case_3(self):
        self.assertFalse(isMonotonic([1, 2, 2, 3, 2, 4]))

    def test_case_4(self):
        self.assertTrue(isMonotonic([1, 1, 1, 1, 1]))

if __name__ == "__main__":
    unittest.main()
