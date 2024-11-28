def ops(x, y):
    return x + y, x - y, x * y, 1e9 if x % y else x // y

a, b, c = map(int, input().split())
print(min(y for x in ops(a, b) for y in ops(x, c) if y >= 0))