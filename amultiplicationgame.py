for line in open(0):
    n = int(line)
    p = w = 1
    while p < n:
        p *= 9 * w or 2
        w ^= 1
    print('Ollie wins.' if w else 'Stan wins.')