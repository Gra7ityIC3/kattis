for _ in range(int(input())):
    a, b, c = map(int, input().split())
    D = b * b - 4 * a * c
    print('YES' if D >= 0 and int(D ** 0.5) ** 2 == D else 'NO')