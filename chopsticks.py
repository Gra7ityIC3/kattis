n, m = map(int, input().split())
s = set()
for _ in range(m):
    x = tuple(map(int, input().split()))
    if x in s:
        s.remove(x)
        n -= 1
    else:
        s.add(x)
print('yes' if n <= 0 else 'no')