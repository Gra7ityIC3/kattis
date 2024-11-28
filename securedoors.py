seen = set()
for _ in range(int(input())):
    action, name = input().split()
    if action == 'entry':
        print(name, 'entered', '(ANOMALY)' * (name in seen))
        seen.add(name)
    else:
        print(name, 'exited', '(ANOMALY)' * (name not in seen))
        seen.discard(name)