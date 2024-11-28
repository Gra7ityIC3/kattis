s = int(input())
print(f'{s}:')
for i in range(2, s // 2 + 2):
    if s % (i + i - 1) in (0, i):
        print(f'{i},{i - 1}')
    if s % i == 0:
        print(f'{i},{i}')