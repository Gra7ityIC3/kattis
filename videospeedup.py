n, p, k = map(int, input().split())
t = [*map(int, input().split()), k]
T = t[0]
for i in range(1, n + 1):
    T += (100 + i * p) / 100 * (t[i] - t[i - 1])
print(T)