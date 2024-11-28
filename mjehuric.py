a = [*map(int, input().split())]
for i in range(1, 5):
    for j in range(5 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            print(*a)