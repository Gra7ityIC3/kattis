while n := int(input()):
    m = [c.upper() for c in input() if not c.isspace()]
    c = [''] * len(m)
    k = 0
    for i in range(n):
        for j in range(i, len(m), n):
            c[j] = m[k]
            k += 1
    print(''.join(c))