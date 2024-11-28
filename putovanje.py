n, c = map(int, input().split())
w = [*map(int, input().split())]
ans = 0
for i in range(n):
    left, curr = c, 0
    for j in range(i, n):
        if w[j] <= left:
            left -= w[j]
            curr += 1
    ans = max(ans, curr)
print(ans)