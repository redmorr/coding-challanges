import pytest

import recursion
import combination
import dp


def make_empty_grid(n, m):
    return [[0 for _ in range(n)] for _ in range(m)]


testcases = [(28, 3, 7),
             (2, 2, 2),
             (3, 3, 2),
             (70, 5, 5),
             (6, 3, 3),
             (22750883079422934966181954039568885395604168260154104734000, 100, 100)]

testcases_obstacles = [[expected, make_empty_grid(n, m)] for expected, n, m in testcases]
testcases_obstacles = testcases_obstacles + [(2, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
                                             (1, [[0, 1], [0, 0]]),
                                             (0, [[1, 0]]),
                                             (0, [[1], [0]]),
                                             (0, [[1]]),
                                             (13, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])]


@pytest.mark.parametrize('expected, grid_width, grid_length', testcases)
@pytest.mark.parametrize('solution_class', [recursion.Solution, combination.Solution, dp.Solution],
                         ids=['Recursion', 'Combination', 'DP'])
def test_unique_paths(solution_class, expected, grid_width, grid_length):
    assert expected == solution_class().uniquePaths(grid_width, grid_length)


@pytest.mark.parametrize('expected, grid_width, grid_length', testcases)
@pytest.mark.parametrize('solution_class', [recursion.Solution, combination.Solution, dp.Solution],
                         ids=['Recursion', 'Combination', 'DP'])
def test_unique_paths_rotate_grid(solution_class, expected, grid_width, grid_length):
    assert expected == solution_class().uniquePaths(grid_length, grid_width)


@pytest.mark.parametrize('expected, grid', testcases_obstacles)
@pytest.mark.parametrize('solution_class', [dp.Solution, recursion.Solution], ids=['DP', 'Recursion'])
def test_unique_paths_with_obstacles(solution_class, expected, grid):
    assert expected == solution_class().uniquePathsWithObstacles(grid)
