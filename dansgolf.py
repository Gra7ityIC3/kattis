n, m, k = map(int, input().split())
s = set()
for _ in range(k):
    x, y = map(int, input().split())
    s.add(x - y)
print(len(s))