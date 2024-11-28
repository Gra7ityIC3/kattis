names = {}
for _ in range(int(input())):
    line = input().split()
    names[line[0]] = line[1:]
for _ in range(int(input())):
    first_name = input()
    if first_name in names:
        second_name = names[first_name]
        if second_name:
            print(f'Neibb en {first_name} {second_name[0]} er heima')
        else:
            print('Jebb')
    else:
        print('Neibb')