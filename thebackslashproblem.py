for n, s in zip(*[iter(open(0))] * 2):
    k = 2 ** int(n) - 1
    print(''.join('\\' * k + c if '!' <= c <= '*' or '[' <= c <= ']' else c for c in s), end='')