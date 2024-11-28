n, *t = map(int, open(0))
print('still running' if n % 2 else sum(t[i] - t[i - 1] for i in range(1, n, 2)))