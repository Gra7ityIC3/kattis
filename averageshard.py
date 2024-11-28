for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    a = sum(cs := [*map(int, input().split())]) / n
    b = sum(map(int, input().split())) / m
    print(sum(b < x < a for x in cs))