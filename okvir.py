M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
a = [input() for _ in range(M)]
ans = [['#.'[(i + j) % 2] for j in range(L + N + R)] for i in range(U + M + D)]
for i in range(M):
    for j in range(N):
        ans[U + i][L + j] = a[i][j]
for row in ans:
    print(''.join(row))