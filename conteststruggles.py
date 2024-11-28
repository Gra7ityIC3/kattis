n, k = map(int, input().split())
d, s = map(int, input().split())
a = (d * n - s * k) / (n - k)
print(a if 0 <= a <= 100 else 'impossible')