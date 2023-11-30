import unittest

from lab6 import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):

    def test_empty_strings(self):
        result = boyer_moore_search("", "")
        self.assertEqual(result, [])

    def test_empty_needle(self):
        result = boyer_moore_search("abcdef", "")
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        result = boyer_moore_search("", "abc")
        self.assertEqual(result, [])

    def test_exact_match(self):
        result = boyer_moore_search("abcabcabc", "abc")
        self.assertEqual(result, [0, 3, 6])

    def test_partial_match(self):
        result = boyer_moore_search("abababab", "bab")
        self.assertEqual(result, [1, 5])

    def test_no_match(self):
        result = boyer_moore_search("abcdefg", "xyz")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

