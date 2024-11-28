from collections import deque

for _ in range(int(input())):
    p = input()
    n = int(input())
    x = deque(input()[1:-1].split(','))
    rev = False
    for c in p:
        if c == 'R':
            rev = not rev
        elif n:
            del x[-1 * rev]
            n -= 1
        else:
            print('error')
            break
    else:
        print(f"[{','.join(reversed(x) if rev else x)}]")