n = int(input())
print('?', *range(1, n + 1))
print('!', int(input()) - n * n * (n + 1) // 2)