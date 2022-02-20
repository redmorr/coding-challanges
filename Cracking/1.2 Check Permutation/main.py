def is_permutation(s, t):
    if len(s) != len(t):
        return False

    letters = {}

    for l in s:
        letters[l] = letters.get(l, 0) + 1

    for l in t:
        try:
            letters[l] -= 1
            if letters[l] < 0:
                return False
        except KeyError:
            return False

    return True
