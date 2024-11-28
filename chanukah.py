for _ in range(int(input())):
    k, n = map(int, input().split())
    print(k, n * (n + 3) // 2)