n, t = map(int, input().split())
d = [0] * n
s = [0] * n
for i in range(n):
    d[i], s[i] = map(int, input().split())
lo, hi = -min(s), 1001000
while hi - lo >= 1e-6:
    mid = (lo + hi) / 2
    if sum(d[i] / (s[i] + mid) for i in range(n)) <= t:
        hi = mid
    else:
        lo = mid
print(hi)