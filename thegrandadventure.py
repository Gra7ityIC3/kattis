for _ in range(int(input())):
    stack = []
    for c in input():
        if c == '.': continue
        if c in '$|*':
            stack.append(c)
        elif not stack or stack.pop() != {'b': '$', 't': '|', 'j': '*'}[c]:
            print('NO')
            break
    else:
        print('NO' if stack else 'YES')