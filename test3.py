import unittest
from lab3 import TreeNode, sum_of_depths

class TestSumOfDepths(unittest.TestCase):
    def test_sum_of_depths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        expected_result = 6
        
        result = sum_of_depths(root)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
