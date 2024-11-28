from collections import Counter

s, t = open(0)
print(''.join(Counter(t) - Counter(s)))