c = 0
for _ in range(n := int(input())):
    c += 1
    x = int(input())
    while c < x:
        print(c)
        c += 1
if c == n:
    print('good job')