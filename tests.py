import unittest
from lab_2 import simplify_time_ranges  

class TestSimplifyTimeRanges(unittest.TestCase):
    
    def test_empty_input(self):
        self.assertEqual(simplify_time_ranges([]), [])

    def test_single_range(self):
        ranges = [(0, 1)]
        self.assertEqual(simplify_time_ranges(ranges), [(0, 1)])

    def test_non_overlapping_ranges(self):
        ranges = [(0, 1), (2, 3), (4, 5)]
        self.assertEqual(simplify_time_ranges(ranges), [(0, 1), (2, 3), (4, 5)])

    def test_overlapping_ranges(self):
        ranges = [(0, 2), (1, 3), (4, 5)]
        self.assertEqual(simplify_time_ranges(ranges), [(0, 3), (4, 5)])

    def test_mixed_ranges(self):
        ranges = [(0, 2), (1, 3), (4, 5), (7, 8), (7, 10)]
        self.assertEqual(simplify_time_ranges(ranges), [(0, 3), (4, 5), (7, 10)])

    def test_example_ranges(self):
        time_ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        self.assertEqual(simplify_time_ranges(time_ranges), [(0, 1), (3, 8), (9, 12)])

if __name__ == '__main__':
    unittest.main()
