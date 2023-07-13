def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_thousandth_prime():
    count = 0
    num = 2
    while count < 1000:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1


thousandth_prime = find_thousandth_prime()
print(thousandth_prime)
