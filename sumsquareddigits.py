for _ in range(int(input())):
    k, b, n = map(int, input().split())
    ssd = 0
    while n:
        ssd += (n % b) ** 2
        n //= b
    print(k, ssd)