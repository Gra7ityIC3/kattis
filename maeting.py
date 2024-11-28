d = {input(): 0 for _ in range(int(input()))}
for _ in range(int(input())):
    _, *names = input().split()
    for name in names:
        d[name] += 1
for k, v in sorted(d.items(), key=lambda x: -x[1]):
    print(v, k)