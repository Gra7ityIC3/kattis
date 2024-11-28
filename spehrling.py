import os

s1 = input()
s2 = input()
print(len(s1) + len(s2) - 2 * len(os.path.commonprefix((s1, s2))))