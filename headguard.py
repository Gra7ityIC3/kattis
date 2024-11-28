from itertools import groupby

for line in open(0):
    print(''.join(f'{len([*g])}{k}' for k, g in groupby(line.rstrip())))