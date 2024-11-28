birthdays = {}
for _ in range(int(input())):
    s, c, date = input().split()
    c = int(c)
    if date not in birthdays or birthdays[date][1] < c:
        birthdays[date] = s, c
print(len(birthdays))
for s, _ in sorted(birthdays.values()):
    print(s)