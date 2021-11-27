from functools import lru_cache

class Solution:
    def uniquePathsIII(self, grid: [[int]]) -> int:
        obstacles = 0

        n = len(grid[0])
        m = len(grid)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    start = (j, i)
                elif cell == 2:
                    end = (j, i)
                elif cell == -1:
                    obstacles = obstacles + 1

        g = grid

        def dfs(x, y, p):
            path = p[:]
            # print("{}".format(p))

            path.append((x, y))
            if g[y][x] == -1 or (x, y) in p:
                return 0

            if x == end[0] and y == end[1]:
                if len(path) == (n * m) - obstacles:
                    # print(len(path))
                    # print(path)
                    return 1
                else:
                    return 0

            stack = []

            if x > 0:
                stack.append((x - 1, y))
            if x < n - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < m - 1:
                stack.append((x, y + 1))

            return sum([dfs(x, y, path) for x, y in stack])

        return dfs(start[0], start[1], [])


print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
