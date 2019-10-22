def largestRectangle(h):
    stack = []
    locs = {x:None for x in h}
    areas = {x:0 for x in h}
    #initial
    h0 = h.pop()
    stack.append(h0)
    locs[h0] = 0
    loc = 0
    debug = []
    while h != []:
        hpop = h.pop()
        loc += 1
        stop = False
        while stack != [] and not stop:
            spop = stack.pop()
            debug.append(spop)
            if hpop > spop:
                stack.append(spop)
                if locs[hpop] == None:
                    locs[hpop] = loc
                else:
                    pass
                stop = True
            elif hpop == spop:
                stop = True
            else:
                area = spop*(loc-locs[spop])
                locs[hpop] = locs[spop]
                locs[spop] = None
                if area > areas[spop]:
                    areas[spop] = area
                else:
                    pass
        stack.append(hpop)
    #final
    loc += 1
    while stack != []:
        spop2 = stack.pop()
        area = spop2*(loc-locs[spop2])
        if area > areas[spop2]:
            areas[spop2] = area
        else:
            pass
    return max(areas.values())