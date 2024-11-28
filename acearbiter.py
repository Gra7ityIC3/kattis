a = b = 0
for i in range(1, int(input()) + 1):
    x, y = map(int, input().split('-'))
    if (x + y + 1) // 2 % 2:
        x, y = y, x
    if any((x < a, y < b, x > 11, y > 11, x == y == 11, max(a, b) == 11 and (a, b) != (x, y))):
       print('error', i)
       break
    a, b = x, y
else:
    print('ok')