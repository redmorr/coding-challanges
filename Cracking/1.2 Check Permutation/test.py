import pytest
from main import is_permutation

testdata = [(True, 'abcde', 'abcde'),
            (True, 'abcde', 'ebcda'),
            (True, 'a', 'a'),
            (False, 'abcd', 'abc'),
            (False, 'abcd', 'abce')]


@pytest.mark.parametrize('expected, string1, string2', testdata)
def test_is_unique(expected, string1, string2):
    assert is_permutation(string1, string2) == expected
