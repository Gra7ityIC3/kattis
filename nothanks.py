n = int(input())
a = sorted(map(int, input().split()))
print(sum(a[i] for i in range(1, n) if a[i] != a[i - 1] + 1) + a[0])