for i in range(1, int(input()) + 1):
    P, K, L = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    print(f'Case #{i}: {sum((1 + i // K) * A[i] for i in range(L))}')