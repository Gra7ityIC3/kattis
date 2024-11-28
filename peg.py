board = [input() for _ in range(7)]
ans = 0
for r in range(7):
    for c in range(7):
        ans += r >= 2 and board[r][c] == 'o' and board[r - 1][c] == 'o' and board[r - 2][c] == '.'
        ans += r <= 4 and board[r][c] == 'o' and board[r + 1][c] == 'o' and board[r + 2][c] == '.'
        ans += c >= 2 and board[r][c] == 'o' and board[r][c - 1] == 'o' and board[r][c - 2] == '.'
        ans += c <= 4 and board[r][c] == 'o' and board[r][c + 1] == 'o' and board[r][c + 2] == '.'
print(ans)