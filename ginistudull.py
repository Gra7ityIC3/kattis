n, *y = map(int, open(0))
y.sort()
print(sum((2 * i - n + 1) * y[i] for i in range(n)) / sum(y) / n)