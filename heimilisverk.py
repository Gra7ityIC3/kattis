seen = set()
for _ in range(int(input())):
    chore = input()
    if chore not in seen:
        seen.add(chore)
        print(chore)