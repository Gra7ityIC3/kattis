input()
words = input().split()
d = dict(input().split() for _ in range(int(input())))
print(' '.join(d[word] for word in words))