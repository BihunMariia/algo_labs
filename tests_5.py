import unittest
from lab_5 import max_experience

class TestCareer(unittest.TestCase):
    def test_example1(self):
        levels = 4
        experience_matrix = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        result = max_experience(levels, experience_matrix)
        self.assertEqual(result, 12)

    def test_example2(self):
        levels = 1
        experience_matrix = [
            [9999]
        ]
        result = max_experience(levels, experience_matrix)
        self.assertEqual(result, 9999)

    def test_example3(self):
        levels = 5
        experience_matrix = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        result = max_experience(levels, experience_matrix)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
