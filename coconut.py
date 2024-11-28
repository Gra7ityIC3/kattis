s, n = map(int, input().split())
players = [(i, 1) for i in range(n)]
i = 0
while n > 1:
    i = (i + s - 1) % n
    p, state = players[i]
    if state == 1:
        players[i] = (p, 2)
        players.insert(i, (p, 2))
        n += 1
    elif state == 2:
        players[i] = (p, 3)
        i = (i + 1) % n
    else:
        del players[i]
        n -= 1
print(players[0][0] + 1)