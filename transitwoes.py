s, t, n = map(int, input().split())
d = [*map(int, input().split())]
b = [*map(int, input().split())]
c = [*map(int, input().split())]
s += d[0]
for i in range(n):
    s = -(-s // c[i]) * c[i] + b[i] + d[i + 1]
print('yes' if s <= t else 'no')