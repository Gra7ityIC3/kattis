from math import sin

while True:
    L, n, C = map(float, input().split())
    if L == -1: break
    if n == 0 or C == 0:
        print(0)
        continue
    L2 = (1 + n * C) * L
    lo, hi = 0, L / 2
    for _ in range(50):
        mid = (lo + hi) / 2
        r = L * L / (8 * mid) + mid / 2
        if 2 * r * sin(L2 / (2 * r)) <= L:
            hi = mid
        else:
            lo = mid
    print(hi)