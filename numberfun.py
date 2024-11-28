for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('Possible' if c in {a + b, abs(a - b), a * b, a / b, b / a} else 'Impossible')