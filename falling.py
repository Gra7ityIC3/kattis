d = int(input())
if d % 2 == 1:
    print((d - 1) // 2, (d + 1) // 2)
elif d % 4 == 0:
    print(d // 4 - 1, d // 4 + 1)
else:
    print('impossible')