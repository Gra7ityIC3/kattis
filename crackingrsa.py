for _ in range(int(input())):
    n, e = map(int, input().split())
    p, q = next((i, n // i) for i in range(2, 1001) if n % i == 0)
    print(pow(e, -1, (p - 1) * (q - 1)))