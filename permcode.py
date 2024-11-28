while x := int(input()):
    S, P, C = input(), input(), input()
    n = len(C)
    d = int(n ** 1.5 + x) % n
    M = [0] * n
    M[d] = P[S.index(C[d])]
    for i in range(1, n):
        j = (d - i) % n
        M[j] = P[S.index(C[j]) ^ S.index(M[(j + 1) % n])]
    print(''.join(M))