input()
f = [*map(int, input().split())]
print('yes' if max(f) // 2 in f else 'no')