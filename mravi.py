n = int(input())
p = [0] * (n + 1)
for _ in range(n - 1):
    a, b, x, t = map(int, input().split())
    p[b] = (a, x / 100, t)
ans = 0
for b, k in enumerate(map(int, input().split()), 1):
    if k == -1: continue
    while b != 1:
        b, x, t = p[b]
        if t: k **= 0.5
        k /= x
    ans = max(ans, k)
print(ans)