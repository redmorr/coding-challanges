import pytest

import solution

# testcases = [(2, [1, 3, 4, 2, 2]),
#              (3, [3, 1, 3, 4, 2]),
#              (1, [1, 1]),
#              (1, [1, 1, 2])]

testcases = [(31, [i for i in range(1, 80)] + [39] + [i for i in range(81, 100)])]


@pytest.mark.parametrize('expected, numbers', testcases)
def test_missing_number(expected, numbers):
    assert expected == solution.Solution().findDuplicate(numbers)
