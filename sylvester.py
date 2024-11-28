for _ in range(int(input())):
    n, x, y, w, h = map(int, input().split())
    for i in range(y, y + h):
        print(*(-1 if bin(i & j).count('1') % 2 else 1 for j in range(x, x + w)))
    print()