n, k = map(int, input().split())
ans = best = 0
for x in map(int, input().split()):
    best = max(best - k, x * 100)
    ans = max(ans, best - x * 100 - k)
print(ans)