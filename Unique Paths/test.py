import pytest

import recursion
import dp

testcases = [(28, 3, 7),
             (2, 2, 2),
             (3, 3, 2),
             (70, 5, 5),
             (6, 3, 3),
             (22750883079422934966181954039568885395604168260154104734000, 100, 100)]


@pytest.mark.parametrize('expected, grid_width, grid_length', testcases)
@pytest.mark.parametrize('solution_class', [recursion.Solution, dp.Solution], ids=['Recursion', 'DP'])
def test_unique_paths(solution_class, expected, grid_width, grid_length):
    assert expected == solution_class().uniquePaths(grid_width, grid_length)


@pytest.mark.parametrize('expected, grid_width, grid_length', testcases)
@pytest.mark.parametrize('solution_class', [recursion.Solution, dp.Solution], ids=['Recursion', 'DP'])
def test_unique_paths_rotate_grid(solution_class, expected, grid_width, grid_length):
    assert expected == solution_class().uniquePaths(grid_length, grid_width)
