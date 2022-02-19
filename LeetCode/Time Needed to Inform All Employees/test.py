import pytest

import dfs

testcases = [(0, 1, 0, [-1], [0]),
             (1, 6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]),
             (21, 7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]),
             (3, 15, 0, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
             (1076, 4, 2, [3, 3, -1, 2], [0, 0, 162, 914]),
             (1, 1000000, 0, [-1] + [0] * (1000000-1), [1] + [0] * (1000000-1))]


@pytest.mark.parametrize('expected, total_employees, head_id, managers, inform_times', testcases)
@pytest.mark.parametrize('solution_class', [dfs.Solution], ids=["DFS"])
def test_numOfMinutes(solution_class, expected, total_employees, head_id, managers, inform_times):
    assert solution_class().numOfMinutes(total_employees, head_id, managers, inform_times) == expected
