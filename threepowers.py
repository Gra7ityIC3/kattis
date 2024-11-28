while n := int(input()):
    print('{', ', '.join(str(3 ** i) for i in range(64) if n - 1 & 1 << i), '}')