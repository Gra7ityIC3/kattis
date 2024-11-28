n, k = map(int, input().split())
cnt = [[0] * k for _ in range(k)]
for _ in range(n):
    t = input()
    for i in range(k):
        for j in range(i + 1, k):
            cnt[ord(t[i]) - 65][ord(t[j]) - 65] += 1
ans = 1
dp = [1] * k
for _ in range(k):
    for i in range(k):
        for j in range(k):
            if cnt[i][j] == n:
                dp[i] = max(dp[i], dp[j] + 1)
                ans = max(ans, dp[i])
print(ans)