for _ in range(int(input())):
    n = int(input())
    ans = ''
    if n % 2:
        ans += 'O'
    if (n ** 0.5).is_integer():
        ans += 'S'
    print(ans or 'EMPTY')