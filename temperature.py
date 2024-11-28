x, y = map(int, input().split())
print(x / (1 - y) if y > 1 else 'IMPOSSIBLE' if x else 'ALL GOOD')