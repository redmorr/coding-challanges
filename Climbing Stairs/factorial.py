from math import factorial


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        for i in range(0, n):
            pos = n - i
            ones = n - 2 * i
            twos = i
            ways = ways + factorial(pos) // factorial(ones) // factorial(twos)
            if ones == 1 or ones == 0:
                break
        return ways
