n = int(input())
lo, hi = 1, 10
while hi - lo > 1e-6:
    mid = (lo + hi) / 2
    if mid ** mid > n:
        hi = mid
    else:
        lo = mid
print(hi)