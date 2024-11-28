n = int(input())
t = [*map(int, input().split())]
print(*min((max(t[i], t[i + 2]), i + 1) for i in range(n - 2))[::-1])