for _ in range(int(input())):
    k, *h = map(int, input().split())
    print(k, sum(h[i] > h[j] for i in range(19) for j in range(i + 1, 20)))