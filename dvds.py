for _ in range(int(input())):
    n, m = int(input()), 1
    for x in map(int, input().split()):
        m += m == x
    print(n - m + 1)