for _ in range(int(input())):
    n = int(input())
    dp = [0] * 151
    dp[0] = 1
    for i in range(n):
        s, p = map(int, input().split())
        for j in range(150, s - 1, -1):
            dp[j] = max(dp[j], dp[j - s] * p / 100)
    print(max(dp[76:]) * 100)