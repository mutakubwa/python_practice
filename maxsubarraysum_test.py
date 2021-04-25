#imports
import unittest
from maxsubarraysum import get_subarray_sum_1, get_subarray_sum_2

class MaxSubArraySum(unittest.TestCase):
    def test_get_subarray_sum_1(self):
        testcase = [1,-5, 3, -2, -8, 3, -9, 1, 1]
        expected = ([1,1],2)
        self.assertEqual(get_subarray_sum_1(testcase), expected)
    
    def test_get_subarray_sum_2(self):
        testcase = [1,-5, 3, -2, -8, 3, -9, 1, 1]
        expected = ([1,1],2)
        self.assertEqual(get_subarray_sum_1(testcase), expected)

if __name__ == '__main__':
    unittest.main()