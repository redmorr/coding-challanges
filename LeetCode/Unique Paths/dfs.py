class Solution:
    def uniquePathsIII(self, grid: [[int]]) -> int:
        obstacles = 0

        n = len(grid[0])
        m = len(grid)
        g = grid

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    start = (j, i)
                elif cell == 2:
                    end = (j, i)
                elif cell == -1:
                    obstacles = obstacles + 1

        walkable_cells = (n * m) - obstacles

        def dfs(x, y, p):
            if (0 > x or x >= n) or (0 > y or y >= m):
                return 0

            if g[y][x] == -1 or (x, y) in p:
                return 0

            path = p[:]
            path.append((x, y))

            if (x, y) == end:
                if len(path) == walkable_cells:
                    return 1
                else:
                    return 0

            return sum([dfs(x, y, path) for x, y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))])

        return dfs(start[0], start[1], [])
