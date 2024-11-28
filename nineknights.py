dr = (-1, 1, -1, 1, -2, 2, -2, 2)
dc = (-2, -2, 2, 2, -1, -1, 1, 1)

board = [input() for _ in range(5)]
k = 0
for r in range(5):
    for c in range(5):
        if board[r][c] == 'k':
            k += 1
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] == 'k':
                    print('invalid')
                    exit()
print('valid' if k == 9 else 'invalid')