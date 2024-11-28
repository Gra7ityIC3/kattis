board = [input() for _ in range(8)]
a, b, c, d = set(), set(), set(), set()
for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            a.add(i)
            b.add(j)
            c.add(i + j)
            d.add(i - j)
print('valid' if len(a) == len(b) == len(c) == len(d) == 8 else 'invalid')