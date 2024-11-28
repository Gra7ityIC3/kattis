while True:
    n, *k = map(int, input().split())
    if n == 0: break
    m = [*input()]
    m += -len(m) % n * [' ']
    print(f"'{''.join(m[i * n + k[j] - 1] for i in range(len(m) // n) for j in range(n))}'")