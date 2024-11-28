n = int(input())
a = [0] * (n - 1)
for i, x in enumerate(map(int, input().split()), 2):
    a[x] = i
print(1, *a)