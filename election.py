binom = [[1] * 51 for _ in range(51)]
for n in range(2, 51):
    for k in range(1, n):
        binom[n][k] = binom[n - 1][k] + binom[n - 1][k - 1]

for _ in range(int(input())):
    n, v1, v2, w = map(int, input().split())
    m = n - v1 - v2
    s = sum(binom[m][i] for i in range(n // 2 + 1 - v1, m + 1))
    if 100 * s > w * 2 ** m:
        print('GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!')
    elif s == 0:
        print('RECOUNT!')
    else:
        print('PATIENCE, EVERYONE!')