import pytest

import solution

testcases = [(['11', '00'], ["01", "10"]),
             (['11', '10'], ["00", "01"]),
             (['101', '010', '100', '110', '000'], ['111', '011', '001'])]


@pytest.mark.parametrize('possible_expected, numbers', testcases)
def test_missing_number(possible_expected, numbers):
    assert solution.Solution().findDifferentBinaryString(numbers) in possible_expected
