b, a = sorted(map(int, input().split()))
if a % b == 0:
    print('win')
else:
    win = True
    while a < 2 * b:
        win = not win
        a, b = b, a - b
    print('win' if win else 'lose')