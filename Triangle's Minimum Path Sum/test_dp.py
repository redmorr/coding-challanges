from unittest import TestCase
from dp import Solution

class TestSolution(TestCase):
    def test_minimum_total(self):
        s = Solution()

        self.assertEqual(11, s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
        self.assertEqual(10, s.minimumTotal([[2], [3, 4], [6, 5, 7]]))
        self.assertEqual(5, s.minimumTotal([[2], [3, 4]]))
        self.assertEqual(2, s.minimumTotal([[2]]))

