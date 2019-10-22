def isValid(s):
    if len(s) <= 1:
        return 'YES'
    else:
        sdict = {x:0 for x in s}
        for i in s:
            sdict[i] += 1
        counts = [y for y in sdict.values()]
        print(counts)
        life = 1
        if 1 in counts:
            counts.remove(1)
            life -= 1
        bar = min(counts[0], counts[1])
        if bar == 1:
            life += 1

        match = 'YES'
        j = 0
        while match == 'YES' and j < len(counts):
            if counts[j] - bar == 1:
                life -= 1
                if life < 0:
                    match = 'NO'
            elif counts[j] - bar == 0:
                pass
            else:
                match = 'NO'
            j += 1
        return match