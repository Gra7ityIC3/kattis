n, m = map(int, open(0))
for i in range(n):
    print('*' * (m // n + (i < m % n)))