n, m = map(int, input().split())
AL = [[] for _ in range(n)]
for _ in range(m):
    k, l = map(int, input().split())
    AL[k].append(l)
    AL[l].append(k)
weight = [0] * n
weight[0] = 1
ex = 0
for i in range(1, 10001):
    new_weight = [0] * n
    for u in range(n - 1):
        for v in AL[u]:
            new_weight[v] += weight[u] / len(AL[u])
    weight = new_weight
    ex += i * weight[-1]
print(ex)