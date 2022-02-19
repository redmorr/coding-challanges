import pytest

import dfs

testcases = [(2, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]),
             (4, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]),
             (0, [[0, 1], [2, 0]])]


@pytest.mark.parametrize('expected, grid', testcases)
def test_unique_paths_with_obstacles(expected, grid):
    assert expected == dfs.Solution().uniquePathsIII(grid)
