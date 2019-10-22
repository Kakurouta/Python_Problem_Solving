def connectedCell(matrix):

    def calarea(m, row, col):
        r = len(m)-1
        c = len(m[0])-1
        ur = min(r, row+1)
        lr = max(0, row-1)        
        uc = min(c, col+1)
        lc = max(0, col-1)

        if m[row][col] == 1:
            m[row][col] = 0
            sub = 1
            for x in range(lr, ur+1):
                for y in range(lc, uc+1):
                    if (x,y) != (row, col):
                        sub += calarea(m, x, y)
            return sub     
        else:
            return 0     

    r = len(matrix)
    c = len(matrix[0])
    areas = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                areas.append(calarea(matrix, i, j))
    return max(areas)