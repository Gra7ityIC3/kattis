n, k = map(int, input().split())
desc = [False] * n
for i in range(n - 2, -1, -1):
    if k >= i + 1:
        desc[i] = True
        k -= i + 1
mn, mx = 1, n
ans = [0] * n
for i in range(n):
    if desc[i]:
        ans[i] = mx
        mx -= 1
    else:
        ans[i] = mn
        mn += 1
print(*ans)