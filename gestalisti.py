guest_list = set()
for _ in range(int(input())):
    c, name = input().split()
    if c == '+':
        guest_list.add(name)
    elif c == '-':
        guest_list.discard(name)
    else:
        print('Jebb' if name in guest_list else 'Neibb')