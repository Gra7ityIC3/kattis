for _ in range(int(input())):
    d = 0
    for x in input().split(','):
        d = d * 60 + int(x or 0)
    print(d)