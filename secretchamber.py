m, n = map(int, input().split())
D = [[i == j for j in range(26)] for i in range(26)]
for _ in range(m):
    a, _, b = input()
    D[ord(a) - 97][ord(b) - 97] = 1
for k in range(26):
    for i in range(26):
        for j in range(26):
            D[i][j] |= D[i][k] & D[k][j]
for _ in range(n):
    s, t = input().split()
    print('yes' if len(s) == len(t) and all(D[ord(a) - 97][ord(b) - 97] for a, b in zip(s, t)) else 'no')