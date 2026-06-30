n, m, k = map(int, input().split())
if m > k:
    print(':(')
else:
    q, r = divmod(sum(map(int, input().split())), k // m)
    print(q + (r > 0))