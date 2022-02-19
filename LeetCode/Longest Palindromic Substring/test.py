import pytest

from main import Solution

testdata = [('a', 'a'),
            ('a', 'ac'),
            ('aa', 'aa'),
            ('bb', 'cbbd'),
            ('abba', 'abba'),
            (49 * 'ab' + 'a', 49 * 'ab' + 'a'),
            ('a' * 1000, 'a' * 1000),
            (495 * 'g', 494 * 'f' + 495 * 'g')]

@pytest.mark.parametrize('expected, word', testdata)
def test1(expected, word):
    assert expected == Solution().longestPalindrome(word)
