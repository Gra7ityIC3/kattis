ans = cur = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    cur += b - a
    ans = max(ans, cur)
print(ans)