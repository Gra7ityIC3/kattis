print('Gnomes:')
for _ in range(int(input())):
    a = [*map(int, input().split())]
    print('Ordered' if a[0] <= a[1] <= a[2] or a[0] >= a[1] >= a[2] else 'Unordered')