for _ in range(int(input())):
    n = len(s := input())
    dp = [[0] * n for _ in range(n)]
    for i in range(n): dp[i][i] = 2
    for j in range(n):
        for i in range(j):
            dp[i][j] = 2 + dp[i][j - 1]
            for k in range(i, j):
                if s[k] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
    print(n + dp[0][-1])