for _ in range(int(input())):
    input()
    x = [*map(int, input().split())]
    print(2 * (max(x) - min(x)))