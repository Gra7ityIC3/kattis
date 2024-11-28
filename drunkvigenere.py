C = input()
K = input()
for i in range(len(C)):
    print(chr((ord(C[i]) + (i % 2 or -1) * ord(K[i])) % 26 + 65), end='')