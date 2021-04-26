#imports
import unittest 
from repetitions import get_num_chars_1, get_num_chars_2, get_num_chars_3

class RepetitionsTest(unittest.TestCase):
    seed_list = ['A','C','G','T']

    def test_get_num_chars_1(self):
        testcase = "AABBBCCGGGTTTTT"
        expected  = 5
        self.assertEqual(get_num_chars_1(testcase, self.seed_list) , expected)
    
    def test_get_num_chars_21(self):
        testcase = "AABBBCCGGGTTTTT"
        expected  = 5
        self.assertEqual(get_num_chars_2(testcase, self.seed_list) , expected)
    
    def test_get_num_chars_22(self):
        testcase = "AABBBCCGGGTTTTT"
        expected  = 5
        self.assertEqual(get_num_chars_2(testcase, self.seed_list) , expected)

    def test_get_num_chars_23(self):
        testcase = "AAAAAAAAAA"
        expected  = 10
        self.assertEqual(get_num_chars_2(testcase, self.seed_list) , expected)

    def test_get_num_chars_24(self):
        testcase = "ACACACACAC"
        expected  = 1
        self.assertEqual(get_num_chars_2(testcase, self.seed_list) , expected)

    def test_get_num_chars_4(self):
        testcase = "AABBBCCGGGTTTTTAA"
        expected  = 5
        self.assertEqual(get_num_chars_3(testcase, self.seed_list) , expected)

if __name__ == '__main__':
    unittest.main()