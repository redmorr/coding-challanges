import pytest
from main import is_unique

testdata = [(True, 'abcd'),
            (True, 'abcdefgh'),
            (True, 'a'),
            (False, 'abcda')]

@pytest.mark.parametrize('expected, input', testdata)
def test_is_unique(expected, input):
    assert is_unique(input) == expected
