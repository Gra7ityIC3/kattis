n = int(input())
A = [*map(int, input().split())]
L, R = [A[0]] * n, [A[-1]] * n
for i in range(1, n):
    L[i] = max(A[i], L[i - 1])
for i in range(n - 2, -1, -1):
    R[i] = min(A[i], R[i + 1])
ans = A[0] < R[1]
ans += L[-2] < A[-1]
for i in range(1, n - 1):
    ans += L[i - 1] < A[i] < R[i + 1]
print(ans)