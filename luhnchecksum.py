for _ in range(int(input())):
    s = input()
    print('FAIL' if sum(sum(divmod(int(s[~i]) << i % 2, 10)) for i in range(len(s))) % 10 else 'PASS')