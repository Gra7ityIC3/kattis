for line in open(0):
    m, p, l, e, r, s, n = map(int, line.split())
    for _ in range(n):
        m, p, l = p // s, l // r, m * e
    print(m)