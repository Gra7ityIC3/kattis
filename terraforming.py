changes = {
    'ocean': 0,
    'oxygen': 0,
    'temperature': -30,
}

for _ in range(int(input())):
    parameter, change = input().split()
    changes[parameter] += int(change[1:])

if changes['ocean'] >= 9 and changes['oxygen'] >= 14 and changes['temperature'] >= 8:
    print('liveable')
else:
    print('not liveable')