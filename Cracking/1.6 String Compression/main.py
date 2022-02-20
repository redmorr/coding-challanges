def compress(s):
    count = 1
    list = []
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            list.append(s[i-1])
            list.append(str(count))
            count = 1

    list.append(s[-1])
    list.append(str(count))

    compressed = ''.join(list)
    if len(compressed) < len(s):
        return compressed
    else:
        return s
