total = 0
for _ in range(int(input())):
    _, direction, count = input().split()
    count = int(count)
    if direction == 'IN':
        total += count
    else:
        total -= count
print(total or 'NO STRAGGLERS')