for _ in range(int(input())):
    l = len(s := input())
    print(next(i for i in range(1, l + 1) if (s[:i] * (l // i + 1)).startswith(s)))