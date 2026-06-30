from math import ceil

small = medium = large = 0
for _ in range(int(input())):
    s, l = input().split()
    l = int(l)
    if s == 'S':
        small += l
    elif s == 'M':
        medium += l
    else:
        large += l
print(ceil(small / 6) + ceil(medium / 8) + ceil(large / 12))