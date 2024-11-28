n, *c = map(int, open(0))
c.sort()
print(next((n - i for i in range(n) if c[i] >= n - i), 0))