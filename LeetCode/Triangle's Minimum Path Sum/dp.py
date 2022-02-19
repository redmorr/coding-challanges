import math


class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp = {0: triangle[0][0]}

        for row in triangle[1:]:
            new_dp = {}
            for i in dp.keys():
                new_dp[i] = min(new_dp.get(i, math.inf), dp[i] + row[i])
                new_dp[i + 1] = min(new_dp.get(i + 1, math.inf), dp[i] + row[i + 1])
            dp = new_dp

        return min(dp.values())
