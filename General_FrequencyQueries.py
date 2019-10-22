def freqQuery(queries):
    dic = {}
    ans = []
    ndic = {}

    def add_ndict(x):
        if x <= 0:
            pass
        elif x not in ndic:
            ndic[x] = 1
        else:
            ndic[x] += 1
    def sub_ndict(y):
        if y <= 0:
            pass
        elif y not in ndic:
            pass
        else:
            ndic[y] -= 1

    for q in queries:
        if q[0] == 1:
            if q[1] in dic:
                sub_ndict(dic[q[1]])
                dic[q[1]] += 1
                add_ndict(dic[q[1]])
            else:
                dic[q[1]] = 1
                add_ndict(1)
        elif q[0] == 2:
            if q[1] in dic:
                sub_ndict(dic[q[1]])
                dic[q[1]] = max(0, dic[q[1]]-1)
                add_ndict(dic[q[1]])
            else:
                pass
            
        else:
            if q[1] in ndic:
                if ndic[q[1]] > 0:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                ans.append(0)
    return ans