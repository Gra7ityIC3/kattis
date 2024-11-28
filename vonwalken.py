d = float(input().split()[0])
lo, hi = 0, 1
steps = dist = 0
for c in map(int, input().split()):
    steps += c
    dist += d
    lo = max(lo, dist - steps)
    hi = min(hi, dist - steps + 1)
    if lo > hi:
        print('impossible')
        break
else:
    print('possible')