input()
stack = []
for c in input():
    if c in '([{':
        stack.append(c)
    elif not stack or stack.pop() != {')':'(', ']':'[', '}':'{'}[c]:
        print('Invalid')
        break
else:
    print('Invalid' if stack else 'Valid')