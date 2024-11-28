m, s = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(m)]
ans = set()
for j in range(s):
    for i in range(m):
        ans.add(a[i][j])
    if len(ans) == j + 1:
        print(j + 1)
        print(*sorted(ans))
        break