b, c, d, l = map(int, input().split())
possible = False
for x in range(l // b + 1):
    for y in range((l - b * x) // c + 1):
        if (l - b * x - c * y) % d == 0:
            possible = True
            print(x, y, (l - b * x - c * y) // d)
if not possible:
    print('impossible')