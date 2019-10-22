def lilysHomework(arr):

    def helperlily(arr, k):      
        sarr = sorted(arr)
        sarrd = {}
        for pos1, val1 in enumerate(sarr):
            sarrd[val1] = pos1
        lpos = [0]*len(arr)
        newarr = [sarrd[x] for x in arr]
        #ex: arr=[1,5,3,2] => sarr=[1,2,3,5]
        #    sarrd={1:0,2:1,3:2,5:3} => newarr = [0,3,2,1]
        for pos, val in enumerate(newarr):
            lpos[val] = pos
        swap = 0
        for i in range(len(newarr)):
            if k == 0:
                if newarr[i] != i:
                    swap += 1
                    lpos[newarr[i]] = lpos[i]
                    newarr[i], newarr[lpos[i]] = newarr[lpos[i]], newarr[i]
            else:
                if newarr[i] != len(arr)-1-i:
                    swap += 1
                    lpos[newarr[i]] = lpos[len(arr)-1-i]
                    newarr[i], newarr[lpos[len(arr)-1-i]] = newarr[lpos[len(arr)-1-i]], newarr[i]
        return swap
    
    ans1 = helperlily(arr, 0)
    ans2 = helperlily(arr, 1)  
    return min(ans1, ans2)