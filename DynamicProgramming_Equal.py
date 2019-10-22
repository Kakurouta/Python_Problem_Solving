def equal(arr):
    def counter(n):
        i = n%5
        c = n//5 + i//2 + i%2
        return c

    mina = min(arr)
    rarr = [x-mina for x in arr]
    rarr1 = [x-mina+1 for x in arr]
    rarr2 = [x-mina+2 for x in arr]
    rarr5 = [x-mina+5 for x in arr]

    count = [0]*4
    for k in range(len(arr)):
        count[0] += counter(rarr[k])
        count[1] += counter(rarr1[k]) 
        count[2] += counter(rarr2[k])
        count[3] += counter(rarr5[k])

    return min(count)
