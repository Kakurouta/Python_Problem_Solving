def countSwaps(a):
    count = 0
    finish = False
    i = len(a)-1
    while not finish and i > 0:
        finish = True
        for j in range(i):
            if a[j] > a[j+1]:
                finish = False
                count += 1
                a[j], a[j+1] = a[j+1], a[j]
    print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(count, a[0], a[-1]))