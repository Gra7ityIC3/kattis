print(k := int(input()).bit_length())
print(*(2 ** i for i in range(k)))