import unittest 
from weird_algorithm import weird_algo


class WeirdAlgorithmTest(unittest.TestCase):
    def test_weird_algo(self):
        testcase = 6
        expected  = 1
        self.assertEqual(weird_algo(testcase), expected)


if __name__ == '__main__':
    unittest.main()