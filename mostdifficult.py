from random import randint

primes = []
bs = [True] * 10001
for i in range(3, 10001, 2):
    if bs[i]:
        for j in range(i * i, 10001, i):
            bs[j] = False
        primes.append(i)

def is_prime(n):
    if n < 10001: return bs[n]
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(3):
        x = pow(randint(2, n - 2), d, n)
        for _ in range(s):
            y = x * x % n
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

for _ in range(int(input())):
    x = int(input())
    if x % 2:
        print(2 if is_prime(x + 2) else -1)
    else:
        print(next((p for p in primes if is_prime(x + p)), -1))