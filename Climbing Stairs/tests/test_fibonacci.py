import common
from fibonacci import Solution
from unittest import TestCase


class TestFibonacci(TestCase):

    def test_multiple(self):
        s = Solution()
        for (n, answer) in common.answers.items():
            self.assertEqual(answer, s.climbStairs(n))

    def test_big_number(self):
        s = Solution()
        self.assertEqual(common.big_answer, s.climbStairs(common.big_n))
