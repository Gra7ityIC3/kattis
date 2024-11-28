n = int(input())
a = input().split()
for i in range(n - 1):
    if len(a[i]) == len(a[i + 1]):
        b1 = '9' + a[i][1:]
        b2 = '1' + a[i + 1][1:] if len(a[i]) > 1 else '0'
        if int(b1) > int(a[i + 1]):
            a[i] = b1
            print(*a)
            break
        if int(a[i]) > int(b2):
            a[i + 1] = b2
            print(*a)
            break
else:
    print('impossible')