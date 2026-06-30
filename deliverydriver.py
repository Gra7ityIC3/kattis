costs = [*map(int, input().split())]
T = [[0] * 3 for _ in range(3)]
T[0][1] = T[1][0] = costs[0]
T[0][2] = T[2][0] = costs[1]
T[1][2] = T[2][1] = costs[2]
n = int(input())
profits = [[*map(int, input().split())] for _ in range(3)]
dp = [profits[city][0] for city in range(3)]
for day in range(1, n):
    dp = [
        profits[curr][day] + max(dp[prev] - T[prev][curr] for prev in range(3))
        for curr in range(3)
    ]
print(max(dp))