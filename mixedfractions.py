while True:
    a, b = map(int, input().split())
    if a == 0: break
    print(f'{a // b} {a % b} / {b}')