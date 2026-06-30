ans = cur = 0
for _ in range(int(input())):
    s, t = map(int, input().split())
    if s > t:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
print(ans)