for i in range(1, int(input()) + 1):
    r, p, d = map(int, input().split())
    ingredients = [0] * r
    for j in range(r):
        name, weight, percentage = input().split()
        if percentage == '100.0':
            main_weight = float(weight) * d / p
        ingredients[j] = (name, float(percentage) / 100)
    print('Recipe #', i)
    for name, percentage in ingredients:
        print(name, percentage * main_weight)
    print('-' * 40)