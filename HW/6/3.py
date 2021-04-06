def isprime(a):
    if a < 2:
        return False
    for x in range(2, a, 1):
        if a % x == 0:
            return False
        else:
            return True

print(isprime(37))
print(isprime(18))
print(isprime(11))
print(isprime(3))