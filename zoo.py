from collections import Counter

i = 1
while n := int(input()):
    print(f'List {i}:')
    for k, v in sorted(Counter(input().split()[-1].lower() for _ in range(n)).items()):
        print(f'{k} | {v}')
    i += 1