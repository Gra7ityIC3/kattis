n = int(input())
stack = []
for x in map(int, input().split()):
    if stack and stack[-1] == x:
        del stack[-1]
    else:
        stack.append(x)
print('impossible' if stack else 2 * n)