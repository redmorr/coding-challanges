import pytest

import large_data
import brute_force
import kadane

small_testdata = [(1, [1]),
                  (23, [5, 4, -1, 7, 8]),
                  (6, [-2, 1, -3, 4, -1, 2, 1, -5, 4])]


@pytest.mark.parametrize('expected, input_array', small_testdata)
@pytest.mark.parametrize('solution_class', [brute_force.Solution, kadane.Solution], ids=["Brute Force", "Kadane"])
def test_small_examples(solution_class, expected, input_array):
    s = solution_class()
    assert expected == s.maxSubArray(input_array)


large_testdata = [(-10000, [-10000] * 100000),
                  (11081, large_data.full_input_array)]


# Brute force approach results in Time Limit Exceeded on large arrays, so we skip it, we know it will fail


@pytest.mark.parametrize('expected, input_array', large_testdata)
@pytest.mark.parametrize('solution_class', [kadane.Solution], ids=["Kadane"])
def test_large_examples(solution_class, expected, input_array):
    s = solution_class()
    assert expected == s.maxSubArray(input_array)
