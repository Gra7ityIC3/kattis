N, Q = map(int, input().split())
A = sorted(map(int, input().split()))
p = [A[0]] * N
for i in range(1, N):
    p[i] = p[i - 1] + A[i]
for B in map(int, input().split()):
    print(p[B - 1])