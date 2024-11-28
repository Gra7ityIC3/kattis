while True:
    n, m = map(int, input().split())
    if n == 0: break
    best = (0, 0, 0)
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= m:
            best = max(best, (a / b, a, b))
    _, a, b = best
    if a == b == 0:
        print('No suitable tickets offered')
    else:
        print(f'Buy {a} tickets for ${b}')