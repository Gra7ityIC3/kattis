from collections import Counter

a, b = Counter(open(0)).most_common(2)
print(a[0] if a[1] > b[1] else 'Runoff!')