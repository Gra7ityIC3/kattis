for i in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    print(f"Case #{i}: {'OFF' if (k + 1) % 2 ** n else 'ON'}")