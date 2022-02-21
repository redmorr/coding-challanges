def is_unique(s):
    hasht = {}
    for l in s:
        val = hasht.get(l, 0)
        if val == 0:
            hasht[l] = 1
        else:
            return False
    return True
