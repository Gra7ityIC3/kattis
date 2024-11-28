from collections import Counter

d = {input(): input() for _ in range(int(input()))}
a, b = Counter(input() for _ in range(int(input()))).most_common(2)
print(d[a[0]] if a[1] > b[1] else 'tie')