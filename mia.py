while True:
    a, b, c, d = map(int, input().split())
    if a == 0: break
    p1 = a + b == 3, a == b, max(a, b), min(a, b)
    p2 = c + d == 3, c == d, max(c, d), min(c, d)
    if p1 == p2:
        print('Tie.')
    elif p1 > p2:
        print('Player 1 wins.')
    else:
        print('Player 2 wins.')