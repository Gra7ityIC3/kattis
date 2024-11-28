n, m = map(int, input().split())
n += 2
print('Arnar' if m < n - n // 3 else 'Unnar')