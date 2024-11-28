dp = [0] * 26
for c in input():
    i = ord(c) - 97
    dp[i] = max(dp[i], max(dp[:i], default=0) + 1)
print(26 - max(dp))