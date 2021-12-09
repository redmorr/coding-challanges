import pytest
import iterate_and_check
import sums
import xor

testcases = [(2, [3, 0, 1]),
             (2, [0, 1]),
             (8, [9, 6, 4, 2, 3, 5, 7, 0, 1]),
             (1, [0]),
             (10**4, [i for i in range(10**4)])]


@pytest.mark.parametrize('expected, numbers', testcases)
@pytest.mark.parametrize('solution_class', [sums, xor, iterate_and_check], ids=['Sums', 'XOR', 'Iterate and check'])
def test_missing_number(solution_class, expected, numbers):
    assert expected == solution_class.Solution().missingNumber(numbers)
