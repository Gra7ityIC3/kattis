d = {}
for _ in range(int(input())):
    c, p = input().split()
    d[c] = d.get(c, 0) + float(p[1:])
    print(c, f'${d[c]:.2f}')