MOD = 10 ** 9

def matMul(a, b):
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += a[i][k] * b[k][j]
                ans[i][j] %= MOD
    return ans

def matPow(base, p):
    ans = [[1, 0], [0, 1]]
    while p:
        if p & 1:
            ans = matMul(ans, base)
        base = matMul(base, base)
        p >>= 1
    return ans

for _ in range(int(input())):
    k, y = map(int, input().split())
    print(k, matPow([[1, 1], [1, 0]], y)[0][1])