def stepPerms(n):
    tmp = {x:None for x in range(1, n+1)}
    def istepPerms(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            if tmp[n] != None:
                pass
            else:
                tmp[n] = istepPerms(n-1) + istepPerms(n-2) + istepPerms(n-3)
            return tmp[n]
    return istepPerms(n)