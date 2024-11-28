d = {}
for _ in range(int(input())):
    d.setdefault(*input().split())
for k, v in [*d.items()][:12]:
    print(k, v)