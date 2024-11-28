from collections import defaultdict

d = defaultdict(set)
for _ in range(int(input())):
    name, course = input().rsplit(' ', 1)
    d[course].add(name)
for k, v in sorted(d.items()):
    print(k, len(v))