from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.__helper(m - 1, n - 1)

    @lru_cache(maxsize=None)
    def __helper(self, i, j):
        if i > 0 and j > 0:
            return self.__helper(i - 1, j) + self.__helper(i, j - 1)
        if i == 0 or j == 0:
            return 1
