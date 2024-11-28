n, *d = map(int, open(0))
print(min(d[i] + d[i - 2] for i in range(n)))