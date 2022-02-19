class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        smaller = min(m - 1, n - 1)
        paths = 1
        div = 1
        for i in range(smaller):
            paths = paths * total // div
            total = total - 1
            div = div + 1

        return paths
