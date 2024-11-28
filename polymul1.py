for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    m = int(input())
    b = [*map(int, input().split())]
    ans = [0] * (n + m + 1)
    for i in range(n + 1):
        for j in range(m + 1):
            ans[i + j] += a[i] * b[j]
    print(n + m)
    print(*ans)