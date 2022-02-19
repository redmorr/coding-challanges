class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    # Redeclare method from above with better memory complexity to compare code
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        # Slicing '[:]' or 'list()' to copy 'obstacleGrid[0]' by value instead of by reference
        result = list(obstacleGrid[0])

        for i, item in enumerate(obstacleGrid[0]):
            if item == 1:
                for j in range(i, len(obstacleGrid[0])):
                    result[j] = 0
                break
            else:
                result[i] = 1

        for row in obstacleGrid[1:]:
            if row[0] == 1:
                result[0] = 0
            for i, col in enumerate(row[1:]):
                if col == 1:
                    result[i + 1] = 0
                else:
                    result[i + 1] = result[i + 1] + result[i]

        return result[-1]
