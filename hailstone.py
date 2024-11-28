h = lambda n: n == 1 or n + (h(3 * n + 1) if n % 2 else h(n // 2))
print(+h(int(input())))