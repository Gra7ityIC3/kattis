n, m = map(int, input().split())
t = [int(input()) for _ in range(m)]
n = min(n, sum(t))
ans = [0] * m
i = 0
while n:
    if t[i]:
        t[i] -= 1
        ans[i] += 1
        n -= 1
    i = (i + 1) % m
print(*ans)