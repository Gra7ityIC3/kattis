l, r = map(int, input().split())
print(f'Odd {2 * max(l, r)}' if l != r else f'Even {l + r}' if l else 'Not a moose')