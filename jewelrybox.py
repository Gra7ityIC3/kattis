for _ in range(int(input())):
    x, y = map(int, input().split())
    h = (x + y - (x * x - x * y + y * y) ** 0.5) / 6
    print((x - 2 * h) * (y - 2 * h) * h)