import unittest
from mergesort import sort

class MergeSortTest(unittest.TestCase):

    def test_sort1(self):
        testcase = [3]
        expected = [3]
        self.assertEqual(sort(testcase), expected)

    
    def test_sort2(self):
        testcase = [3,2]
        expected = [2,3]
        self.assertEqual(sort(testcase), expected)

    
    def test_sort3(self):
        testcase = [5,1]
        expected = [1,5]
        self.assertEqual(sort(testcase), expected)

    
    def test_sort4(self):
        testcase = [5,1,3]
        expected = [1,3,5]
        self.assertEqual(sort(testcase), expected)
    
    def test_sort5(self):
        testcase = [5,1,3,0]
        expected = [0,1,3,5]
        self.assertEqual(sort(testcase), expected)
    
    
    
    def test_mergesort6(self):
        testcase = [3,2,1]
        expected = [1,2,3]
        self.assertEqual(sort(testcase), expected)
    
    

    def test_mergesort1(self):
        testcase = [1,3,8,2,9,2,5,6]
        expected = [1,2,2,3,5,6,8,9]
        self.assertEqual(sort(testcase), expected)
    
    
if __name__ == '__main__':
    unittest.main()