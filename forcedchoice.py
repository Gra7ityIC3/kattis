n, p, s = map(int, input().split())
for _ in range(s):
    m, *c = map(int, input().split())
    print('KEEP' if p in c else 'REMOVE')