for _ in range(int(input())):
    a = b = 1
    for _ in range(int(input())):
        a, b = b, (a + b) % 1000000007
    print(b)