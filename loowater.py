while True:
    n, m = map(int, input().split())
    if n == 0: break
    d = sorted(int(input()) for _ in range(n))
    h = sorted(int(input()) for _ in range(m))
    i = j = ans = 0
    while i < m and j < n:
        if h[i] >= d[j]:
            ans += h[i]
            j += 1
        i += 1
    print('Loowater is doomed!' if j < n else ans)