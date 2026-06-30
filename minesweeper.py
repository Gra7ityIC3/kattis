n, m, k = map(int, input().split())
board = [['.' for _ in range(m)] for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = '*'
for row in board:
    print(''.join(row))