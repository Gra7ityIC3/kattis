for i, line in enumerate(open(0), 1):
    _, *X = map(int, line.split())
    print(f'Case {i}: {min(X)} {max(X)} {max(X) - min(X)}')