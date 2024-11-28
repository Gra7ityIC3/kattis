n, p, m = map(int, input().split())
score = {input(): 0 for _ in range(n)}
seen = set()
for _ in range(m):
    name, points = input().split()
    score[name] += int(points)
    if score[name] >= p and name not in seen:
        seen.add(name)
        print(name, 'wins!')
if not seen:
    print('No winner!')