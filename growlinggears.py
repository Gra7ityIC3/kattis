for _ in range(int(input())):
    best = Tmax = 0
    for i in range(1, int(input()) + 1):
        a, b, c = map(int, input().split())
        T = b * b / (4 * a) + c
        if T > Tmax:
            Tmax = T
            best = i
    print(best)