i = 1
while n := int(input()):
    print('SET', i)
    stack = []
    for j in range(n):
        if j % 2:
            stack.append(input())
        else:
            print(input())
    while stack:
        print(stack.pop())
    i += 1