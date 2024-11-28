for _ in range(int(input())):
    x1, y1 = map(float, input().split())
    ans = 'curse the darkness'
    for _ in range(int(input())):
        x2, y2 = map(float, input().split())
        if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= 64:
            ans = 'light a candle'
    print(ans)