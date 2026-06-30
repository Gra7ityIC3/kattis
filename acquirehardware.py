h, w = map(int, input().split())
dp = [0] * (w + 1)
for i in range(h):
    for j, c in enumerate(input(), 1):
        dp[j] = max(dp[j], dp[j - 1]) + (c == 'I')
print(dp[w])