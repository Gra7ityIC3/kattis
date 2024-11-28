n = int(input())
p = sorted(float(input().split()[1]) for _ in range(n))
print(sum((n - i) * p[i] for i in range(n)))