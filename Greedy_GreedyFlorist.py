def getMinimumCost(k, c):
    c.sort()
    cost = 0
    mul = k
    while c != []:
        cost += c.pop()*(mul//k)
        mul += 1
    return cost