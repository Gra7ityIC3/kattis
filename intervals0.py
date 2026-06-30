n, k = map(int, input().split())
freq = [0] * 24
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        freq[i] += 1
print(sum(x >= k for x in freq))