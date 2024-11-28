T, C, G = map(input().count, 'TCG')
print(T * T + C * C + G * G + 7 * min(T, C, G))