n = int(input())
seen = {prev := input()}
for i in range(1, n):
    word = input()
    if word[0] != prev[-1] or word in seen:
        print(f'Player {i % 2 + 1} lost')
        break
    seen.add(prev := word)
else:
    print('Fair game')