n, m = map(int, input().split())
seq = ['fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0) or str(i) for i in range(1, m + 1)]
print(min((sum(a != b for a, b in zip(seq, input().split())), i) for i in range(n))[1] + 1)