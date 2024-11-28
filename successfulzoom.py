n = int(input())
x = [*map(int, input().split())]
for k in range(1, n // 2 + 1):
    if all(x[i] < x[i + k] for i in range(k - 1, n - k, k)):
        print(k)
        break
else:
    print('ABORT!')