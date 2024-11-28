for line in open(0):
    a, op, b = line.split()
    print(pow(int(a), int(b), 10000) if op == '^' else eval(line) % 10000)