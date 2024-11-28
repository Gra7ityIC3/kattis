n = int(input())
AM = [[*map(int, input().split())] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if AM[i][j]:
            for k in range(j + 1, n):
                ans += AM[j][k] & AM[k][i]
print(ans)