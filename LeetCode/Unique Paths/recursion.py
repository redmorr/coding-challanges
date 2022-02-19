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

    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        self.grid = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.__helper_obstacles(m - 1, n - 1)

    @lru_cache(maxsize=None)
    def __helper_obstacles(self, i, j):
        # Logic can be optimized, but it's easier to understand this way
        if self.grid[i][j] == 1:
            return 0
        if i > 0 and j > 0:
            return self.__helper_obstacles(i - 1, j) + self.__helper_obstacles(i, j - 1)
        if i == 0 and j == 0:
            return 1
        if i == 0:
            return self.__helper_obstacles(0, j - 1)
        if j == 0:
            return self.__helper_obstacles(i - 1, 0)
