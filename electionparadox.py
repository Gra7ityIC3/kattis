n = int(input())
p = sorted(map(int, input().split()))
print(sum(p[i] // 2 + p[~i] for i in range(n // 2 + 1)) - p[n // 2])