def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    def size(i,j):
        if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + sum(size(i2,j2) for i2 in range(i-1,i+2) for j2 in range(j-1,j+2))
        return 0
    return max(size(i,j) for i in range(n) for j in range(m))
