for _ in range(int(input())):
    n = int(input())
    ans, pos = [0] * n, -1
    for i in range(1, n + 1):
        for j in range(i + 1):
            pos = (pos + 1) % n
            while ans[pos]:
                pos = (pos + 1) % n
        ans[pos] = i
    print(*ans)