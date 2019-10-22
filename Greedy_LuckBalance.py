def luckBalance(k, contests):
    balance = 0
    imp = []
    for i in contests:
        if i[1] == 0:
            balance += i[0]
        else:
            imp.append(i[0])
    simp = sorted(imp)
    lsimp = len(simp)
    for j in range(min(lsimp, k)):
        balance += simp.pop()
    while simp != []:
        balance -= simp.pop()
    return balance