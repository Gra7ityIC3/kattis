s = [*map(int, input())]
for _ in range(int(input())):
    print(''.join(chr((ord(c) - 65) * d % 26 + 65) for c, d in zip(input(), s)))