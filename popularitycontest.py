n, m = map(int, input().split())
ans = [~i for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    ans[a - 1] += 1
    ans[b - 1] += 1
print(*ans)