n = int(input())
AM = [[*map(int, input().split())] for _ in range(n)]
EL = [(i + 1, j + 1, AM[i][j]) for i in range(n) for j in range(n) if AM[i][j] > 0]
print(len(EL))
for u, v, c in EL:
    print(u, v, c)