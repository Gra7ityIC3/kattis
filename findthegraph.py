n = int(input())
deg = [0] * n
for i in range(n):
    print(f'? 1 {i + 1}')
    deg[i] = int(input())
AM = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        print(f'? 2 {i + 1} {j + 1}')
        if deg[i] + deg[j] - 2 == int(input()):
            AM[i][j] = AM[j][i] = 1
print('!')
for row in AM: print(*row)