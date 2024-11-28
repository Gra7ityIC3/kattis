f = lambda n: '{' + ','.join(map(f, range(n))) + '}'
print(f(int(input())))