n, *a = map(int, open(0))
a.sort()
print(sum(1 << i - j - 1 for i in range(n) for j in range(i) for k in range(j) if a[k] + a[j] > a[i]))