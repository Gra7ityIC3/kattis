n = int(input())
a = sorted(map(int, input().split()))
print(sum((a[j + 1] - a[j]) ** 2 for j in range(n - 1)))