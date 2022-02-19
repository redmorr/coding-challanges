import pytest

import brute_force
import dfs


small_testdata = [(2, '12'),
                  (3, '226'),
                  (0, '0'),
                  (0, '06'),
                  (121393, 25 * '1')]

large_testdata = [(20365011074, 50 * '1'),
                  (573147844013817084101, 100 * '1')]


@pytest.mark.parametrize('expected, code', small_testdata)
@pytest.mark.parametrize('solution_class', [dfs.Solution, brute_force.Solution], ids=['DFS', 'Brute Force'])
def test_decodings_number_small(solution_class, expected, code):
    assert expected == solution_class().numDecodings(code)


# Brute force approach results in Time Limit Exceeded on large arrays, so we skip it, we know it will fail

@pytest.mark.parametrize('expected, code', large_testdata)
@pytest.mark.parametrize('solution_class', [dfs.Solution], ids=['DFS'])
def test_decodings_number_large(solution_class, expected, code):
    assert expected == solution_class().numDecodings(code)
