n, p, q = map(int, input().split())
print('opponent' if (p + q) // n % 2 else 'paul')