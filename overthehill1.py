alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
n = int(input())
A = [[*map(int, input().split())] for _ in range(n)]
m = [alphabet.find(c) for c in input()]
m += -len(m) % n * [36]
print(''.join(alphabet[sum(A[j][k] * m[i + k] for k in range(n)) % 37] for i in range(0, len(m), n) for j in range(n)))