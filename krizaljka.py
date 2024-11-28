A, B = input().split()
n, m = len(A), len(B)
i, j = next((i, j) for j in range(n) for i in range(m) if B[i] == A[j])
grid = [['.'] * n for _ in range(m)]
for k in range(n):
    grid[i][k] = A[k]
for k in range(m):
    grid[k][j] = B[k]
for row in grid:
    print(''.join(row))