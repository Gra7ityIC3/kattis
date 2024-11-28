N, T = map(int, input().split())
t = sorted(int(input()) for _ in range(N))
print('YES' if all(t[i] > T * i for i in range(N)) else 'NO')