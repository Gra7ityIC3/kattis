n = len(s := input())
for r in range(int(n ** 0.5), 0, -1):
    if n % r == 0:
        break
print(''.join(s[i + j * r] for i in range(r) for j in range(n // r)))