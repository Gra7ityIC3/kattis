def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if rank[x] < rank[y]: x, y = y, x
    parent[y] = x
    if rank[x] == rank[y]: rank[x] += 1

n, m, q = map(int, input().split())
EL = set()
for _ in range(m):
    u, v = map(int, input().split())
    EL.add((u, v))
queries = [0] * q
for i in range(q):
    t, u, v = map(int, input().split())
    if t == 0: EL.remove((u, v))
    queries[~i] = (t, u, v)
parent = [*range(n)]
rank = [0] * n
for u, v in EL:
    union(u, v)
ans = []
for t, u, v in queries:
    if t:
        ans.append('safe' if find(u) == find(v) else 'unsafe')
    else:
        union(u, v)
for i in range(len(ans)):
    print(ans[~i])