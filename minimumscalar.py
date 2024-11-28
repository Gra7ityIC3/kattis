for i in range(1, int(input()) + 1):
    input()
    v1 = sorted(map(int, input().split()))
    v2 = sorted(map(int, input().split()), reverse=True)
    print(f'Case #{i}: {sum(x * y for x, y in zip(v1, v2))}')