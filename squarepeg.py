l, r = map(int, input().split())
print('fits' if l <= 2 ** 0.5 * r else 'nope')