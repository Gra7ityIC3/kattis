lo, hi = 1, 1000
while True:
    print(mid := (lo + hi) // 2)
    s = input()
    if s == 'lower':
        hi = mid - 1
    elif s == 'higher':
        lo = mid + 1
    else:
        break