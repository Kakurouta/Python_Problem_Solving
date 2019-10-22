def triplets(a, b, c):
    count = 0
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    a1 = a.pop()
    c1 = c.pop()
    b1 = b[::-1]

    for q in b1:
        while a1 > q and a != []:
            a1 = a.pop()
        while c1 > q and c != []:
            c1 = c.pop()
        if a1 <= q:
            a.append(a1)
            a1 = q
        if c1 <= q:
            c.append(c1)
            c1 = q
        count += len(a)*len(c)
    return count