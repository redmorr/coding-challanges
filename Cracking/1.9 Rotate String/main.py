def is_substring(s, t):
    return t in s


def is_rotation(s, t):
    if len(s) != len(t) or len(s) == 0:
        return False
    return is_substring(2 * s, t)
