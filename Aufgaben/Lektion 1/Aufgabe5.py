prime = 2
counter = 0


def isprime():
    for indexFor in range(2, prime):
        if prime % indexFor == 0:
            return False
    return True


while counter < 1000:
    if isprime():
        counter += 1
    prime += 1

print(prime - 1)
