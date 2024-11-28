for _ in range(int(input())):
    m = int(input())
    j = (m, 1, m + 1, 0)[m % 4] ^ m
    print(m - 1 if j else m)
    print(*(i for i in range(1, m + 1) if i != j))