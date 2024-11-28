class FTree:
    def __init__(self, n):
        self.n = n
        self.ft = [0] * (n + 1)

    def lsone(self, s):
        return s & -s

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)
        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)
        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

n, q = map(int, input().split())
v = [0, *map(int, input().split())]
p = [0, *map(int, input())]
ft = [0, *(FTree(n) for _ in range(6))]
for i in range(1, n + 1):
    ft[p[i]].update(i, 1)
for _ in range(q):
    op, a, b = map(int, input().split())
    if op == 1:
        ft[p[a]].update(a, -1)
        ft[b].update(a, 1)
        p[a] = b
    elif op == 2:
        v[a] = b
    else:
        print(sum(v[i] * ft[i].query(a, b) for i in range(1, 7)))