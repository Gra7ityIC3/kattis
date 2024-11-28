n = len(s := input())
freq = [0] * 4
for c in s:
    if c == '_':
        freq[0] += 1
    elif c.islower():
        freq[1] += 1
    elif c.isupper():
        freq[2] += 1
    else:
        freq[3] += 1
for i in range(4):
    print(freq[i] / n)