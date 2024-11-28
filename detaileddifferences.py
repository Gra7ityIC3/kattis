for _ in range(int(input())):
    print(a := input())
    print(b := input())
    print(''.join('*.'[x == y] for x, y in zip(a, b)))
    print()