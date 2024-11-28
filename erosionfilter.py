n = int(input())
A = [*map(int, input().split())]
p, s = [A[0]] * n, [A[-1]] * n
for i in range(1, n):
    p[i] = p[i - 1] / 2 + A[i]
for i in range(n - 2, -1, -1):
    s[i] = s[i + 1] / 2 + A[i]
print(*(p[i] + s[i] - A[i] for i in range(n)))