n = int(input())
a = [*map(int, input().split()), 0]
print(sum(max(0, a[i] - a[i + 1] - 1, 0) for i in range(n)))