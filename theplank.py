a = b = 0
c = 1
for _ in range(int(input())):
    a, b, c = b, c, a + b + c
print(c)