def matMul(a, b):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += a[i][k] * b[k][j]
    return ans

def matPow(base, p):
    ans = [[i == j for j in range(n)] for i in range(n)]
    while p:
        if p & 1:
            ans = matMul(ans, base)
        base = matMul(base, base)
        p >>= 1
    return ans

n, m, s, t = map(int, input().split())
AM = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    AM[x][y] = AM[y][x] = 1
ans = matPow(AM, t)
print(sum(ans[s][i] for i in range(n)))