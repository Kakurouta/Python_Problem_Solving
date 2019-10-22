def pairs(k, arr):
    a = set(arr)
    b = set(x+k for x in arr)
    return len(a&b)