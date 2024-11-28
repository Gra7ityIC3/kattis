from itertools import product, islice

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
print(*islice(map(''.join, product(consonants, vowels, consonants, consonants)), int(input())), sep='\n')