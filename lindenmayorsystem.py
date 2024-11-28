n, m = map(int, input().split())
d = dict(input().split(' -> ') for _ in range(n))
s = input()
for _ in range(m):
    s = ''.join(map(d.get, s, s))
print(s)