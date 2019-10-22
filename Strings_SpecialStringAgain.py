def substrCount(n, s):
    ss = list(s)
    count = 2 #head and tail

    if ss[0] == ss[1]:
        same = 2
    else:
        same = 1

    def side(x, y):
        z = 1
        good = True
        sub = 0
        while x-z >= 0 and x+z <= n-1 and good:
            if ss[x-z] == ss[x+z] == y:
                sub += 1 
                z += 1
            else:
                good = False
        return sub

    def cntsame(c):
        return int(c*(c+1)/2 - c)

    for i in range(1, n-1):
        count += 1
        ns = ss[i+1]
        if ss[i] == ns:
            same += 1
        else:
            count += cntsame(same)
            same = 1
            count += side(i, ns)

    count += cntsame(same)
    return count