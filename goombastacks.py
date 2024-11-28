a = 0
for _ in range(int(input())):
    g, b = map(int, input().split())
    a += g
    if a < b:
        print('impossible')
        break
else:
    print('possible')