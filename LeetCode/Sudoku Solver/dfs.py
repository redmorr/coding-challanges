import copy


class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        n = 9
        fullset = {str(i) for i in range(1, n + 1)}
        result = []

        def subbox(x, y, board):
            a = (x // 3) * 3
            b = (y // 3) * 3
            return {board[j][i] for i in range(a, a + 3) for j in range(b, b + 3) if board[j][i] != '.'}

        def verticals(x, board):
            return {board[i][x] for i in range(n) if board[i][x] != '.'}

        def horizontals(y, board):
            return {i for i in board[y] if i != '.'}

        def dfs(x, y, lb):
            nonlocal result
            if y < n:
                if lb[y][x] != '.':
                    if x + 1 < n:
                        dfs(x + 1, y, lb)
                    elif y + 1 < n:
                        dfs(0, y + 1, lb)
                    else:
                        result = lb
                else:
                    choices = fullset - subbox(x, y, lb) - verticals(x, lb) - horizontals(y, lb)
                    for num in choices:
                        b = copy.deepcopy(lb)
                        b[y][x] = num
                        if x + 1 < n:
                            dfs(x + 1, y, b)
                        elif y + 1 < n:
                            dfs(0, y + 1, b)
                        else:
                            result = b
            else:
                result = lb

        dfs(0, 0, board)

        # Dumb workaround to make the solution accepted, because it's supposed to be modified in-place
        for i in range(9):
            for j in range(9):
                board[i][j] = result[i][j]

        # Added to make tests possible. Remove when submitting the solution
        return board
