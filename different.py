for line in open(0):
    a, b = map(int, line.split())
    print(abs(a - b))