for _ in range(int(input())):
    k, *o = map(int, input().split())
    print(1 + sum(o) - k)