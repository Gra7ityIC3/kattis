lo, hi = 0, 1000
for _ in range(int(input())):
    a, b = map(int, input().split())
    lo = max(a, lo)
    hi = min(b, hi)
print('gunilla has a point' if lo <= hi else 'edward is right')