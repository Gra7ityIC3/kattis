G, S, C = map(int, input().split())
buying_power = 3 * G + 2 * S + C
if buying_power >= 8:
    print('Province or Gold')
elif buying_power >= 6:
    print('Duchy or Gold')
elif buying_power >= 5:
    print('Duchy or Silver')
elif buying_power >= 3:
    print('Estate or Silver')
elif buying_power >= 2:
    print('Estate or Copper')
else:
    print('Copper')