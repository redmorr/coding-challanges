from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m -1, n-1)

    @lru_cache(maxsize=None)
    def dp(self, i, j):
        if i > 0 and j > 0:
            return self.dp(i - 1, j) + self.dp(i, j - 1)
        if i > 0:
            return self.dp(i - 1, 0)
        if j > 0:
            return self.dp(0, j - 1)
        if i == 0 and j == 0:
            return 1

print(Solution().dp(100, 100))
