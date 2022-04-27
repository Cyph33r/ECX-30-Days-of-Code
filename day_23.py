def sieve_of_eratosthenes(end: int) -> list[int]:
    """
Generated all prime number from 2 to end using the Sieve of E
    :param end: limit to the sieve
    :return: a list object containing all prime number from 2 to end
    """
    assert isinstance(end, int), f'Expected one parameter of class int, you pass in a {end.__class__}'  # sanitise input
    assert end > 1, "End should be an integer greater than 1"
    prime = [False] + ([True] * (
            end - 1))  # generate a list of booleans representing if the number at index+1 is a prime number. For
    # example 1 is not a prime number so prime[0+1] is initialized as false
    for i in range(1, end):  # start with 2 i.e. 1+1
        if (i + 1) ** 2 > end:  # check if there is any prime number left
            break
        if prime[i]:  # if the number is a prime mark all its multiples as not prime
            for j in range(((i + 1) ** 2) - 1, end, i + 1):
                prime[j] = False
    return [index + 1 for index, is_prime in enumerate(prime) if is_prime]


if __name__ == '__main__':
    print(sieve_of_eratosthenes(9))
