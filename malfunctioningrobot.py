for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    print(dx + dy + abs(dx - dy) // 2 * 2)