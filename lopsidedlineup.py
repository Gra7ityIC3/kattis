n = int(input())
c = sorted(sum(map(int, input().split())) for _ in range(n))
print(sum(c[~i] - c[i] for i in range(n // 2)) // 2)