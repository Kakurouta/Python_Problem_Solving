def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return None
        else:
            for j in range(max(0, q[i]-2), i):
                if q[j] > q[i]:
                    count += 1
    print(count)