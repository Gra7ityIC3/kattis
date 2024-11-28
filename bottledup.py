s, v1, v2 = map(int, input().split())
for x in range(s // v1, -1, -1):
    if (s - v1 * x) % v2 == 0:
        print(x, (s - v1 * x) // v2)
        break
else:
    print('Impossible')