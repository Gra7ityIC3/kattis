n, q = map(int, input().split())
d = {input(): i for i in range(n)}
for _ in range(q):
    a, b = input().split()
    print(abs(d[a] - d[b]) - 1)