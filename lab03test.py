"""
CSC131 - Computational Thinking, Spring 2018
Missouri State University

Unit test module that tests the `lab03` module.
"""
import unittest
from lab03 import question_1
from lab03 import question_2
from lab03 import question_3
from lab03 import question_4
from lab03 import question_5
from lab03 import question_6
from lab03 import even_filter
from lab03 import find_min


class MyTestCase(unittest.TestCase):
    test_list = []
    test_dict = {}

    def setUp(self):
        self.test_list = list(range(1, 11))
        self.test_dict = {1: "one", 3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"}

    def tearDown(self):
        self.test_list = None
        self.test_dict = None

    def test_question_1(self):
        expected_list = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3]
        actual_list = question_1(self.test_list)
        self.assertListEqual(expected_list, actual_list)

    def test_question_2(self):
        expected_list = [3, 6, 9]
        actual_list = question_2(self.test_list)
        self.assertListEqual(expected_list, actual_list)

    def test_question_3(self):
        expected_str = '12345678910'
        actual_str = question_3(self.test_list)
        self.assertEqual(expected_str, actual_str)

    def test_question_4(self):
        expected_list = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3]
        actual_list = question_4(self.test_list)
        self.assertListEqual(expected_list, actual_list)

    def test_question_5(self):
        expected_list = [3, 6, 9]
        actual_list = question_5(self.test_list)
        self.assertListEqual(expected_list, actual_list)

    def test_question_6(self):
        expected_list = [27, 216, 729]
        actual_list = question_6(self.test_list)
        self.assertListEqual(expected_list, actual_list)

    def test_even_filter(self):
        expected_list = ['four', 'eight', 'ten']
        actual_list = even_filter(self.test_dict)
        self.assertListEqual(expected_list, actual_list)

    def test_find_min_first_less(self):
        expected = -3
        actual = find_min(-3, 4)
        self.assertEqual(expected, actual)

    def test_find_min_second_less(self):
        expected = -3
        actual = find_min(4, -3)
        self.assertEqual(expected, actual)

    def test_find_min_same(self):
        expected = 4
        actual = find_min(4, 4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
