def twoStrings(s1, s2):
    dic = {x:1 for x in s1}
    result = 'NO'
    for c in s2:
        if c in dic:
            result = 'YES'
    return result
