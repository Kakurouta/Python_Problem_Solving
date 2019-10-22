def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        for j in range(1, m+1):
            if i == 0:
                dp[i][j] = a[j-1].islower() and dp[i][j-1]
            elif i != 0:
                if a[j-1] == b[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif a[j-1].upper() == b[i-1]:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
                elif a[j-1].islower():
                    dp[i][j] = dp[i][j-1]
    return "YES" if dp[n][m] else "NO"