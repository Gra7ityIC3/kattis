a = b = c = 0
for _ in range(int(input())):
    x, y, z = input().split()
    a += x == 'J'
    b += y == 'J'
    c += z == 'J'
print(min(a, b, c))