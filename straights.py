input()
freq = [0] * 10001
for x in sorted(map(int, input().split())):
    freq[x] += 1
    freq[x - 1] = max(0, freq[x - 1] - 1)
print(sum(freq))