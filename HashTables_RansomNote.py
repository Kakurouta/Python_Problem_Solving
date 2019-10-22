def checkMagazine(magazine, note):
    mag = {}
    match = 'Yes'
    for word in magazine:
        if word in mag:
            mag[word] += 1
        else:
            mag[word] = 1
    for word2 in note:
        if word2 in mag:
            mag[word2] -= 1
            if mag[word2] < 0:
                match = 'No'
        else:
            match = 'No'
    print(match)