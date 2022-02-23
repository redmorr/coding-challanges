import pytest
from main import is_rotation

testdata = [(True, 'abcde', 'eabcd'),
            (True, 'abcde', 'deabc'),
            (True, 'aaaab', 'aabaa'),
            (False, 'aaaab', 'aaaaa'),
            (False, 'aa', 'aaa'),
            (False, 'aa', ''),
            (False, '', '')]


@pytest.mark.parametrize('expected, string1, string2', testdata)
def test_is_rotation(expected, string1, string2):
    assert is_rotation(string1, string2) is expected

