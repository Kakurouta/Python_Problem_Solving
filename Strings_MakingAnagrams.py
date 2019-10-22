def makeAnagram(a, b):
    charset = 'abcdefghijklmnopqrstuvwxyz'
    dicta = {x:0 for x in charset}
    dictb = {y:0 for y in charset}
    la = list(a)
    lb = list(b)
    count = 0
    while la != []:
        dicta[la.pop()] += 1
    while lb != []:
        dictb[lb.pop()] += 1
    for z in charset:
        count += abs(dicta[z] - dictb[z])
    return count