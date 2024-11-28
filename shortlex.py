for _ in range(int(input())):
    i = int(input())
    k = 0
    while i >= 2 ** k:
        i -= 2 ** k
        k += 1
    print(f'{i:0{k}b}')