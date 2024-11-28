n = int(input())
t = [0] * n
v = [0] * n
for i in range(n):
    t[i], v[i] = map(float, input().split())
print(sum((v[i] + v[i + 1]) * (t[i + 1] - t[i]) for i in range(n - 1)) / 2000)