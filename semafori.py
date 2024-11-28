n, l = map(int, input().split())
t = p = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    t += d - p
    p = d
    while t % (r + g) < r:
        t += 1
print(t + l - p)