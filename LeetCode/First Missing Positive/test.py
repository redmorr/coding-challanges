import pytest
import solution_1
import solution_2
import solution_3

testcases = [(3, [1, 2, 0]),
             (2, [3, 4, -1, 1]),
             (1, [7, 8, 9, 11, 12]),
             (1, [2, 2]),
             (2, [1]),
             (2, [1] * 10000000),
             (1000000, [i for i in range(1000000)])]


@pytest.mark.parametrize('expected, numbers', testcases)
@pytest.mark.parametrize('solution_class', [solution_1, solution_2, solution_3], ids=['Solution 1', 'Solution 2', 'Solution 3'])
def test_first_missing_positive(solution_class, expected, numbers):
    assert expected == solution_class.Solution().firstMissingPositive(numbers)
