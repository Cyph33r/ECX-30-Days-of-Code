def _is_prime(num: int) -> bool:
    """
    Determines if a number is a prime number or not i.e it only whole divisors are 1 and itself
    :param num:the number to be determined
    :returns: True if the :num is a prime number False otherwise
    """
    assert isinstance(num, int), f'Expected a class int for num but a {num.__class__} was passed'
    if num <= 1:  # return false if the parameter is 1 or less since they are not prime numbers
        return False
    is_prime = True
    for i in range(2, num // 2 + 1):  # start half-way since 2 is the lowest divisor
        if num % i == 0:  # check if the number is divisible
            is_prime = False  # if some is_prime becomes False and is returned
            break
    return is_prime


if __name__ == '__main__':
    print(_is_prime(7))
