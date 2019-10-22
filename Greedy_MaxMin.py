def maxMin(k, arr):
    arr.sort()
    a = arr[:-k+1]
    b = arr[k-1:]
    diff = []
    for i in range(len(arr)-k+1):
        diff.append(b[i]-a[i])       
    return min(diff)