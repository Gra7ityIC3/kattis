for _ in range(int(input())):
    k, *a = map(int, input().split())
    print(k, sum(a[i - 1] < min(a[i:j]) > a[j] for i in range(1, 12) for j in range(i + 1, 12)))