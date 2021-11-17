from factorial import Solution
from unittest import TestCase


class TestSolution(TestCase):
    answers = {1: 1,
               2: 2,
               3: 3,
               4: 5,
               5: 8,
               6: 13,
               10: 89,
               20: 10946,
               30: 1346269,
               45: 1836311903}

    def test_multiple(self):
        s = Solution()
        for (n, answer) in self.answers.items():
            self.assertEqual(answer, s.climbStairs(n))

    def test_big_number(self):
        s = Solution()
        self.assertEqual(225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626, s.climbStairs(500))

