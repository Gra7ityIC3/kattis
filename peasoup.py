for _ in range(int(input())):
    peasoup = pancakes = False
    k = int(input())
    name = input()
    for _ in range(k):
        item = input()
        peasoup = peasoup or item == 'pea soup'
        pancakes = pancakes or item == 'pancakes'
    if peasoup and pancakes:
        print(name)
        break
else:
    print('Anywhere is fine I guess')