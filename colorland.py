n = int(input())
board = ['BOPGRY'.find(input()[0]) for _ in range(n)]
cur = best = ans = 0
while cur < n:
    for i in range(6):
        try:
            best = max(best, board.index(i, cur))
        except:
            pass
    cur = best + 1
    ans += 1
print(ans)