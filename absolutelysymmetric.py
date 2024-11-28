n = int(input())
A = [[*map(int, input().split())] for _ in range(n)]
absolutely_symmetric = True
for i in range(n):
    for j in range(n):
        if (A[i][j] + A[j][i]) % 2:
            print(-1)
            exit()
        absolutely_symmetric &= abs(A[i][j]) == abs(A[j][i])
if absolutely_symmetric:
    print(1)
    for row in A: print(*row)
else:
    print(2)
    for i in range(n):
        print(*((A[i][j] + A[j][i]) // 2 for j in range(n)))
    for i in range(n):
        print(*((A[i][j] - A[j][i]) // 2 for j in range(n)))