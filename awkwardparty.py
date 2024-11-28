n = int(input())
prev, ans = {}, n
for i, x in enumerate(map(int, input().split())):
    if x in prev:
        ans = min(ans, i - prev[x])
    prev[x] = i
print(ans)