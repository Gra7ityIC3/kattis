s, p, m, n = map(int, input().split())
t = [*map(int, input().split())]
dp = [0] * (n + 1)
j = 0
for i in range(n):
    while t[j] <= t[i] - m: j += 1
    dp[i + 1] = min(s + dp[i], p + dp[j])
print(dp[n])