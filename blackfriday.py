input()
a = [0] * 7
for i, x in enumerate(map(int, input().split()), 1):
    a[x] = -1 if a[x] else i
print(next((a[i] for i in range(6, 0, -1) if a[i] > 0), 'none'))