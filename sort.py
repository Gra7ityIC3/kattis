from collections import Counter

input()
for k, v in sorted(Counter(map(int, input().split())).items(), key=lambda x: -x[1]):
    print(f'{k} ' * v, end='')