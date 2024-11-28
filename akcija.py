_, *c = map(int, open(0))
c.sort()
print(sum(c) - sum(c[-3::-3]))