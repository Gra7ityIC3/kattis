s, n = map(int, input().split())
a = [*map(int, input().split())]
a.append(a[0] + s)
print(sum((a[i + 1] - a[i] - 2) // 2 for i in range(n)))