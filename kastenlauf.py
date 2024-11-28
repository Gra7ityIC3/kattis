for _ in range(int(input())):
    n = int(input()) + 2
    points = [[*map(int, input().split())] for _ in range(n)]
    D = [[0] * n for _ in range(n)]
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            D[i][j] = D[j][i] = abs(x1 - x2) + abs(y1 - y2) <= 1000
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] |= D[i][k] & D[k][j]
    print('happy' if D[0][n - 1] else 'sad')