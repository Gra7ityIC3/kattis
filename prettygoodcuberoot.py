for line in open(0):
    x = int(line)
    lo, hi = 1, x
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** 3 <= x:
            lo = mid
        else:
            hi = mid - 1
    lo += x - lo ** 3 > (lo + 1) ** 3 - x
    print(lo)