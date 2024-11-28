input()
print('makes sense' if all(x in (str(i), 'mumble') for i, x in enumerate(input().split(), 1)) else 'something is fishy')