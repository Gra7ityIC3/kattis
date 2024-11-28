for line in open(0):
    r, s = map(float, line.split())
    print(round((r * (s + 0.16) / 0.067) ** 0.5))