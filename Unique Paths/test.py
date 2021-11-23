import pytest

import recursion

testcases = [(28, 3, 7),
             (2, 2, 2),
             (3, 3, 2),
             (6, 3, 3),
             (22750883079422934966181954039568885395604168260154104734000, 100, 100)]


@pytest.mark.parametrize('expected, grid_width, grid_length', testcases)
def test_unique_paths(expected, grid_width, grid_length):
    assert expected == recursion.Solution().uniquePaths(grid_width, grid_length)


@pytest.mark.parametrize('expected, grid_width, grid_length', testcases)
def test_unique_paths_rotate_grid(expected, grid_width, grid_length):
    assert expected == recursion.Solution().uniquePaths(grid_length, grid_width)
