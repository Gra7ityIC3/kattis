a = [[False] * 14 for _ in range(4)]
for i in range(0, len(S := input()), 3):
    T = 'PKHT'.find(S[i])
    XY = int(S[i + 1] + S[i + 2])
    if a[T][XY]:
        print('GRESKA')
        break
    a[T][XY] = True
else:
    print(*(13 - sum(a[i][j] for j in range(1, 14)) for i in range(4)), sep=' ')