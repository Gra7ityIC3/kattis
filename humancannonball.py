import math

a = [*map(float, input().split())]
b = [*map(float, input().split())]
n = int(input()) + 2
points = [a, *([*map(float, input().split())] for _ in range(n - 2)), b]
D = [[0] * n for _ in range(n)]
for i in range(1, n):
    D[0][i] = math.dist(a, points[i]) / 5
    for j in range(i + 1, n):
        dist = math.dist(points[i], points[j])
        D[i][j] = D[j][i] = min(dist / 5, 2 + abs(dist - 50) / 5)
for k in range(n):
    for i in range(n):
        for j in range(n):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
print(D[0][-1])