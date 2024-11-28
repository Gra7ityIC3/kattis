input()
stack = []
for i, c in enumerate(input()):
    if c == ' ': continue
    if c in '([{':
        stack.append(c)
    elif not stack or stack.pop() != {')':'(', ']':'[', '}':'{'}[c]:
        print(c, i)
        break
else:
    print('ok so far')