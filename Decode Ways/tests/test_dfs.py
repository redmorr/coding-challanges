from dfs import Solution
from unittest import TestCase


class TestSolution(TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(2, s.numDecodings("12"))

    def test2(self):
        s = Solution()
        self.assertEqual(3, s.numDecodings("226"))

    def test_zero(self):
        s = Solution()
        self.assertEqual(0, s.numDecodings("0"))

    def test_begins_zero(self):
        s = Solution()
        self.assertEqual(0, s.numDecodings("06"))

    def test_quarter_long(self):
        s = Solution()
        self.assertEqual(121393, s.numDecodings(25 * "1"))

    def test_half_long(self):
        s = Solution()
        self.assertEqual(20365011074, s.numDecodings(50 * "1"))

    def test_full_long(self):
        s = Solution()
        self.assertEqual(573147844013817084101, s.numDecodings(100 * "1"))
