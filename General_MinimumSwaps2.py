def minimumSwaps(arr):
    lpos = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        lpos[val] = pos
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            lpos[arr[i]] = lpos[i+1]
            arr[i], arr[lpos[i+1]] = arr[lpos[i+1]], arr[i]
    return swaps

#quicksort may not find the fewest time
#selection sort may not catch up with time limit
#on the basis of consecutive integer from 1 to n... modify selection sort