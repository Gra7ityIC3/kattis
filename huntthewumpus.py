import sys

s, d = int(input()), set()
while len(d) < 4:
    s += s // 13 + 15
    d.add(divmod(s % 100, 10))
m = 0
for line in sys.stdin:
    x1, y1 = divmod(int(line), 10)
    if (x1, y1) in d:
        print('You hit a wumpus!')
        d.remove((x1, y1))
    if d:
        print(min(abs(x1 - x2) + abs(y1 - y2) for x2, y2 in d))
    m += 1
print(f'Your score is {m} moves.')