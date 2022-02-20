import pytest
from main import is_palindrome_permutation

testdata = [(True, 'Tact Coa'),
            (False, 'Tact Coa x'),
            (True, 'aa'),
            (True, 'aaa'),
            (False, 'ab')]


@pytest.mark.parametrize('expected, string', testdata)
def test_is_unique(expected, string):
    assert is_palindrome_permutation(string) == expected
