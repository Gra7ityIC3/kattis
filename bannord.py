s = {*input()}
m = input().split()
for i in range(len(m)):
    if any(c in s for c in m[i]):
        m[i] = '*' * len(m[i])
print(' '.join(m))