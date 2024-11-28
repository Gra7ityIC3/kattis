r, c, zr, zc = map(int, input().split())
for _ in range(r):
    row = input()
    for _ in range(zr):
        print(''.join(c * zc for c in row))