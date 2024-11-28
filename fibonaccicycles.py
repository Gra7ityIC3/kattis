for _ in range(int(input())):
    k = int(input())
    a = b = n = 1
    seen = {}
    while True:
        a, b = b, (a + b) % k
        if b in seen:
            print(seen[b])
            break
        n += 1
        seen[b] = n