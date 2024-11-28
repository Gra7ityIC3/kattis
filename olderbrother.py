def is_prime_power(q):
    if q == 1:
        return False
    for p in range(2, int(q ** 0.5) + 1):
        if q % p == 0:
            while q % p == 0:
                q /= p
            return q == 1
    return True

print('yes' if is_prime_power(int(input())) else 'no')