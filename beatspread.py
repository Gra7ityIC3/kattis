for _ in range(int(input())):
    s, d = map(int, input().split())
    print('impossible' if s < d or (s + d) % 2 else f'{(s + d) // 2} {(s - d) // 2}')