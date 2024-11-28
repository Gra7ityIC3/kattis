n = int(input())
a = [0] * n
for _ in range(n):
    t, i = map(int, input().split())
    a[i - 1] = t
ans, cur = 0, 1
for t in a:
    ans += max(t - cur, 0)
    cur = max(cur, t) + 1
print(ans)