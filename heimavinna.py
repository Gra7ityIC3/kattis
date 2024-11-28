n = 0
for x in input().split(';'):
    s = x.split('-')
    n += len(s) == 1 or int(s[1]) - int(s[0]) + 1
print(n)