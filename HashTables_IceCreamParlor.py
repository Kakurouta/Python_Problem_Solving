def whatFlavors(cost, money):
    costdict = {x:1 for x in cost}
    m2 = money/2
    match = False
    n = False
    if m2 in costdict:
        i1 = cost.index(m2)
        costdict2 = {y:1 for y in cost[i1+1::]}
        if m2 in costdict2:
            match = True
            n = True
            i2 = cost.index(m2, i1+1)
        
    i = 0
    while not match:
        diff = money - cost[i]
        if diff != m2 and diff in costdict.keys():
            match = True
        else:
            i += 1
    if n:
        print(i1+1, i2+1)
    else:
        print(i+1, cost.index(money-cost[i])+1) 
