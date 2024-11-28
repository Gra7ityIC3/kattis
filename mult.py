t = 0
for _ in range(int(input())):
    m = int(input())
    if t == 0:
        t = m
    elif m % t == 0:
        print(m)
        t = 0