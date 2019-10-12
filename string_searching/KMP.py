def failure_func(s):
    table = [-1] * (len(s) + 1)
    pos, cnd = 1, 0
    while pos < len(s):
        if s[pos] == s[cnd]:
            table[pos] = table[cnd]
        else:
            table[pos] = cnd
            cnd = table[cnd]

            while cnd >=0 and s[cnd] != s[pos]:
                cnd = table[cnd]
        pos += 1
        cnd += 1
    table[pos] = cnd
    return table
# find s2 in s1
def search(s1, s2):
    if len(s2) > len(s1):
        return None
    j, k, nP = 0, 0, 0
    table = failure_func(s2)

    while j < len(s1):
        if s1[j] == s2[k]:
            j += 1
            k += 1
            if k == len(s2):
                return j - k
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1
    return None

search('ABC ABCDAB ABCDABCDABDE','ABCDABD')
