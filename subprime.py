l, h = map(int, input().split())
p = input()
primes = [0]
bs = [True] * 1299710
for i in range(2, 1299710):
    if bs[i]:
        for j in range(i * i, 1299710, i):
            bs[j] = False
        primes.append(i)
print(sum(p in str(primes[i]) for i in range(l, h + 1)))