n, m = map(int, input().split())
ans = [f'T{i}' for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(ans.index, input().split())
    if i > j: ans.insert(i, ans.pop(j))
print(*ans)