n, m = map(int, input().split())
print(2 % m if n == 0 else (5 * pow(2, n - 1, m) - 1) % m)