import unittest
from bubblesort import bubblesort

class TwoQueens(unittest.TestCase):
    def test_bubblesort(self):
        testcase = [1,3,8,2,9,2,5,6]
        expected = [1,2,2,3,5,6,8,9]
        self.assertEqual(bubblesort(testcase), expected)

if __name__ == '__main__':
    unittest.main()