for i in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    image = [input() for _ in range(R)]
    print('Test', i)
    for r in range(R):
        print(*(image[~r][~c] for c in range(C)), sep='')