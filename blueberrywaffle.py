r, f = map(int, input().split())
print('down' if round(f / r) % 2 else 'up')