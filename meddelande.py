n, m = map(int, input().split())
print(''.join(c for _ in range(n) for c in input() if c != '.'))