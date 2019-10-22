def superDigit(n, k):
    n, k = int(n), int(k)
    def _sup(i):
        if i < 10:
            return i
        else:
            return _sup(i//10) + i % 10
    def _splitsup(k):
        if len(str(k)) > 10:
            sub = 0
            while k > 0:
                sub += _sup(k % 10000000000)
                k = k // 10000000000
            return sub
        else:
            return _sup(k)
    def __sup(j):
        if j < 10:
            return j
        else:
            return __sup(_splitsup(j))
    return __sup(__sup(n)*k)