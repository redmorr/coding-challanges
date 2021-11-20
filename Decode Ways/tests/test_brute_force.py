from brute_force import Solution
from unittest import TestCase


class TestSolution(TestCase):

    def test_quarter_long(self):
        s = Solution()
        self.assertEqual(0, s.numDecodings(25 * "1"))

    # Brute force is too inefficient and execution exponentially too much time
    # def test_half_long(self):
    #     s = Solution()
    #     self.assertEqual(0, s.numDecodings(50 * "1"))
