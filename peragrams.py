from collections import Counter
print(max(0, sum(v % 2 for v in Counter(input()).values()) - 1))