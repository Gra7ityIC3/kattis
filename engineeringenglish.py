seen = set()
for line in open(0):
    for i in range(len(line := line.split())):
        if line[i].lower() in seen:
            line[i] = '.'
        else:
            seen.add(line[i].lower())
    print(' '.join(line))