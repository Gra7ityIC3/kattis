a = [0] * 45
for _ in range(int(input())):
    for i, x in enumerate(input()):
        a[i] += ord(x) + 1j
print(''.join(chr(int(z.real / z.imag)) for z in a if z))