while (n := int(input())) != -1:
    d = p = 0
    for _ in range(n):
        s, t = map(int, input().split())
        d += s * (t - p)
        p = t
    print(d, 'miles')