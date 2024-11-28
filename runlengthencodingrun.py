from itertools import groupby

c, _, *s = input()
if c == 'E':
    print(''.join(f'{k}{len([*g])}' for k, g in groupby(s)))
else:
    print(''.join(s[i] * int(s[i + 1]) for i in range(0, len(s), 2)))