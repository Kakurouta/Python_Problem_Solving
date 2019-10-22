def candies(n, arr):
    larr = len(arr)
    count = []
    count.append(1)
    rarr = arr[::-1]
    rcount = []
    rcount.append(1)
    if larr == 1:
        return 1
    else:
        for i in range(0, larr-1):
            if arr[i+1] > arr[i]:
                count.append(count[i]+1)
            else:
                count.append(1)
            if rarr[i+1] > rarr[i]:
                rcount.append(rcount[i]+1)
            else:
                rcount.append(1)
        rrcount = rcount[::-1]
        for i in range(0, larr):
            count[i] = max(count[i], rrcount[i])
        return sum(count)