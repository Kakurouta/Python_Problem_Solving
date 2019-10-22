def sherlockAndAnagrams(s):
    ords = [ord(x)-96 for x in s]
    count = 0

    for n in range(len(s)):
        tmp = {}
        for m in range(len(s)-n):
            p = str(sorted(ords[m:m+n+1]))
            if p in tmp:
                count += tmp[p]
                tmp[p] += 1
            else:
                tmp[p] = 1     
    return count