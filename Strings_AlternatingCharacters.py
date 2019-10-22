def alternatingCharacters(s):
    count = 0
    tmp = s[0]
    for i in range(1, len(s)):
        if tmp == s[i]:
            count += 1
        else:
            tmp = s[i]
    return count