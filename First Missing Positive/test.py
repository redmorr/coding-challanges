import pytest
import solution

testcases = [(3, [1, 2, 0]),
             (2, [3, 4, -1, 1]),
             (1, [7, 8, 9, 11, 12]),
             (2, [1])]


@pytest.mark.parametrize('expected, numbers', testcases)
def test_first_missing_positive(expected, numbers):
    assert expected == solution.Solution().firstMissingPositive(numbers)
