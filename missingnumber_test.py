import unittest 
from missingnumber import missing_number_1, missing_number_2

class MissingNumber_Test(unittest.TestCase):
    def test_missingnumber1(self):
        testcase1 = 5
        testcase2 = [2,2,3,4,5]
        expected = 1
        self.assertEqual(missing_number_1(testcase1, testcase2), expected)

    def test_missingnumber2(self):
        testcase1 = 5
        testcase2 = [2,2,5,4,1]
        expected = 3
        self.assertEqual(missing_number_1(testcase1, testcase2), expected)

    def test_missingnumber3(self):
        testcase1 = 5
        testcase2 = [5,5,3,2,4]
        expected = 1
        self.assertEqual(missing_number_1(testcase1, testcase2), expected)
    
    def test_missingnumber4(self):
        testcase1 = 5
        testcase2 = [2,2,3,4,5]
        expected = 1
        self.assertEqual(missing_number_2(testcase1, testcase2), expected)

    def test_missingnumber5(self):
        testcase1 = 5
        testcase2 = [2,2,5,4,1]
        expected = 3
        self.assertEqual(missing_number_2(testcase1, testcase2), expected)

    def test_missingnumber6(self):
        testcase1 = 5
        testcase2 = [5,5,3,2,4]
        expected = 1
        self.assertEqual(missing_number_2(testcase1, testcase2), expected)

if __name__ == '__main__':
    unittest.main()