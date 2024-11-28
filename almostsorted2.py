n = int(input())
a = [*map(int, input().split())]
i = j = -1
for k in range(n - 1):
    if a[k] > a[k + 1]:
        if i == -1:
            i = k
        j = k + 2
a[i:j] = a[i:j][::-1]
print('Yes' if all(a[i] <= a[i + 1] for i in range(n - 1)) else 'No')