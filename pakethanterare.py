n, b = map(int, input().split())
t = [*map(int, input().split())]
d = dict(input().split() for _ in range(n))
for i in range(b):
    ans = 0
    for _ in range(t[i]):
        s, v = input().split()
        ans += int(d[s]) - int(v)
    print(ans)