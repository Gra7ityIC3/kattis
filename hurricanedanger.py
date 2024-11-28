for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    ans, min_d = [], 1e9
    for _ in range(int(input())):
        city, x, y = input().split()
        d = abs(a * int(x) + b * int(y) + c)
        if d < min_d:
            min_d = d
            ans = [city]
        elif d == min_d:
            ans.append(city)
    print(*ans)