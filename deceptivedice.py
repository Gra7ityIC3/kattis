n, k = map(int, input().split())
ex = 0
for _ in range(k):
    m = int(ex)
    ex = ((n - m) * (n + m + 1) / 2 + m * ex) / n
print(ex)