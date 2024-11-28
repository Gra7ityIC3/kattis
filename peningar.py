n, d = map(int, input().split())
a = [*map(int, input().split())]
ans = i = 0
while a[i]:
    ans += a[i]
    a[i] = 0
    i = (i + d) % n
print(ans)