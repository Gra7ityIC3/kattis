s = input()
a, b = 10 ** 9, 0
if s[0] == s[-1]:
    a, b = b, a
for i in range(1, len(s) // 2):
    if s[i] == s[~i]:
        a, b = min(a, b + 2), min(a + 2, b + 1)
    else:
        a, b = min(a + 2, b + 1), min(a, b + 1)
print(min(a, b + 1))