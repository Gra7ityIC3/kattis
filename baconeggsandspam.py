from collections import defaultdict

while n := int(input()):
    d = defaultdict(list)
    for _ in range(n):
        name, *items = input().split()
        for item in items:
            d[item].append(name)
    for item, names in sorted(d.items()):
        print(item, ' '.join(sorted(names)))
    print()