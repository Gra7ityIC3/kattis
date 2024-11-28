n, *a = map(int, open(0))
print(sum(max(a[i], a[i + 1]) for i in range(n - 1)))