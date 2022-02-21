def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_palindrome_permutation(s):
    letters = {}
    evens = 0
    odds = 0
    s = s.replace(' ', '').lower()

    for l in s:
        letters[l] = letters.get(l, 0) + 1

    for v in letters.values():
        if is_even(v):
            evens += 1
        else:
            odds += 1

    if is_even(len(s)):
        if odds > 0:
            return False
    else:
        if is_even(odds):
            return False

    return True
