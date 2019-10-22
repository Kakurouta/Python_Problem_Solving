def sol(que,a,b=0):
    if a == 1:
        que.append(b)
    elif a == 2:
        if que:
            que.pop(0)
        else:
            pass
    else:
        if que:
            print(que[0])
        else:
            pass

q = int(input())
que = []
for i in range(q):
    x = input()
    if len(x) == 1:
        a = x
    else:
        [a,b] = x.split(' ')
    sol(que,int(a),int(b))
