a, b = map(int, input().split())
s1 = s2 = 0
for _ in range(a):
    v, c = map(int, input().split())
    s1 += v * c
for _ in range(b):
    v, c = map(int, input().split())
    s2 += v * c
print('same' if s1 == s2 else 'different')