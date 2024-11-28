MOD = 10 ** 9 + 7
n = int(input())
stack = [0]
for token in input().split():
    if token == '(':
        stack.append(len(stack) % 2)
    else:
        x = stack.pop() if token == ')' else int(token)
        stack.append((stack.pop() + x if len(stack) % 2 else stack.pop() * x) % MOD)
print(stack[0])