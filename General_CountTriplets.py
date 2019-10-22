def countTriplets(arr, r):
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    count = 0
    for k in arr:
        count += d3[k]
        d3[k*r] += d2[k]
        d2[k*r] += 1

    return count