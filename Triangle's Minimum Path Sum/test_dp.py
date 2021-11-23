import pytest

from dp import Solution

testdata = [(11, [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]),
            (10, [[2], [3, 4], [6, 5, 7]]),
            (5, [[2], [3, 4]]),
            (2, [[2]])]


@pytest.mark.parametrize('expected, triangle', testdata)
def test_minimum_path_sum(expected, triangle):
    assert expected == Solution().minimumTotal(triangle)
