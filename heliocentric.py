for i, line in enumerate(open(0), 1):
    e, m = map(int, line.split())
    d = 0
    while (e + d) % 365 or (m + d) % 687:
        d += 1
    print(f'Case {i}: {d}')