n = int(input())
a = [*map(int, input().split())]
dp = [0, a[0]]
for i in range(1, n):
    dp = [dp[1], min(dp) + a[i]]
print(min(dp))