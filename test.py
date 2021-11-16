from main import Solution
from unittest import TestCase


class TestSolution(TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("cbbd"), "bb")

    def test2(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("abba"), "abba")

    def test21(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("abbba"), "abbba")

    def test3(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("a"), "a")

    def test4(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("a"), "a")

    def test5(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("ac"), "a")

    def test51(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("aa"), "aa")

    def test6(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"),
                        "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")

    def test7(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("a" * 1000), "a" * 1000)

    def test8(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"),
                        "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")

    def test9(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("f" * 10 + "g" * 11), "g" * 11)

    def test91(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("ab" * 10 + "a"), "ab" * 10 + "a")
