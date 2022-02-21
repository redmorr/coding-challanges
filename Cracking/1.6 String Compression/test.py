import pytest
from main import compress

testdata = [('a2b1c5a3', 'aabcccccaaa'),
            ('a2b1c5a3x1', 'aabcccccaaax'),
            ('a', 'a'),
            ('aa', 'aa'),
            ('aab', 'aab'),
            ('a4b1', 'aaaab'),
            ('a1000b1000c1000', '{}{}{}'.format('a' * 1000, 'b' * 1000, 'c' * 1000))]


@pytest.mark.parametrize('expected, string', testdata)
def test_is_unique(expected, string):
    assert compress(string) == expected
