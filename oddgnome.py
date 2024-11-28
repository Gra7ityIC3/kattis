for _ in range(int(input())):
    g, *a = map(int, input().split())
    print(next(i + 1 for i in range(1, g) if a[i] != a[i - 1] + 1))