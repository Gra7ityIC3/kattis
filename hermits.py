n = int(input())
a = [0, *map(int, input().split())]
streets = a.copy()
for _ in range(int(input())):
    i, j = map(int, input().split())
    streets[i] += a[j]
    streets[j] += a[i]
print(min((streets[i], i) for i in range(1, n + 1))[1])