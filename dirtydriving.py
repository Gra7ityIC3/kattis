n, p = map(int, input().split())
d = sorted(map(int, input().split()))
print(max(p * (i + 1) - d[i] for i in range(n)) + d[0])