s = input()
x = y = 0
for c in s:
    x = x * 2 + (c in '13')
    y = y * 2 + (c in '23')
print(len(s), x, y)