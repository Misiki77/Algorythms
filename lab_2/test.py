import unittest

from main import find_sum


class TestFindTripletWithSum(unittest.TestCase):
    def test_sum_exist(self):
        A = [1, 2, 3, 4, 5]
        P = 10
        result = find_sum(A, P)
        self.assertEqual(result, True)

    def test_sum_not_exist(self):
        A = [1, 2, 3, 4, 5]
        P = 13
        result = find_sum(A, P)
        self.assertEqual(result, False)

    def test_empty_array(self):
        A = []
        P = 10
        result = find_sum(A, P)
        self.assertEqual(result, False)

    def test_small_array(self):
        A = [1, 2]
        P = 3
        result = find_sum(A, P)
        self.assertEqual(result, False)