stack = []
for _ in range(int(input())):
    line = input()
    if line == 'Present!':
        del stack[-1]
    else:
        stack.append(line)
print('\n'.join(stack) if stack else 'No Absences')