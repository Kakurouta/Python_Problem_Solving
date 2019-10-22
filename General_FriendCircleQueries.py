def maxCircle(queries):
    maxp = 2
    p = {} #record member:parent
    c = {} #record member:childcount
    ans = []

    def rootparent(p, mem):
        while p[mem] != mem:
            mem = p[mem]
        return mem

    for q in queries:
        if q[0] not in p:
            p[q[0]] = q[0]
            c[q[0]] = 1
        if q[1] not in p:
            p[q[1]] = q[1]
            c[q[1]] = 1

        p0 = rootparent(p, q[0])
        p1 = rootparent(p, q[1])

        if p0 != p1:
            if c[p0] > c[p1]:
                p[p1] = p0 
                c[p0] = c[p0] + c[p1]        
                if c[p0] > maxp:
                    maxp = c[p0]
            else:
                c[p1] = c[p0] + c[p1]
                p[p0] = p1
                if c[p1] > maxp:
                    maxp = c[p1]            

        ans.append(maxp)
    return ans