ul = ur = ll = lr = 8
for _ in range(int(input())):
    s = input()
    if s[0] == '+':
        ul = s[3] != 'b' and ul - 1
    elif s[0] == '-':
        ll = s[3] != 'b' and ll - 1
    elif s[1] == '+':
        ur = s[3] != 'b' and ur - 1
    else:
        lr = s[3] != 'b' and lr - 1
print(0 if ul > 0 and ll > 0 else 1 if ur > 0 and lr > 0 else 2)