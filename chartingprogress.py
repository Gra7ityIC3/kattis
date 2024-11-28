total = 0
for line in open(0):
    if line == '\n':
        total = 0
        print()
    else:
        count = line.count('*')
        print(f"{'.' * (len(line) - 1 - count - total)}{'*' * count}{'.' * total}")
        total += count