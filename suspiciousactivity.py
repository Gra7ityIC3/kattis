ans = 0
for _ in range(int(input())):
    u, d = map(int, input().split())
    if u % 8 != 0 and (d < 1 or d > 10000):
        ans += 1
print(ans)