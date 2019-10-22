from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.ordlist = [ord(x) for x in name]
        
    def __repr__(self):
        pass
    def comparator(self, a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            i = 0
            while a.ordlist[i] == b.ordlist[i] and i < min(len(a.name), len(b.name))-1:
                i += 1
            if a.ordlist[i] > b.ordlist[i]:
                return 1
            elif a.ordlist[i] < b.ordlist[i]:
                return -1
            elif len(a.name) < len(b.name):
                return -1
        return 0