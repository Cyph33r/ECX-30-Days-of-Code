def gcf(num1: int, num2: int) -> int:
    """
    Calculate the GCF(Greatest Common Factor) of two numbers
    :param num1: first number must not be zero or equal to num2 and must be an integer
    :param num2: second number must not be zero or equal to num1 and must be an integer
    :return: The GCF of num1 and num2 as an integer
    """
    higher = num1  # copy the numbers into another variable
    lower = num2
    assert isinstance(higher,
                      int), f"This function takes in two parameters of class int you provided a {higher.__class__}"
    assert isinstance(lower,
                      int), f"This function takes in two parameters of class int you provided a {lower.__class__}"
    assert higher != lower, "Parameters cannot be the same"
    assert higher > 0 and lower > 0, "Both parameters should be above 0"
    while True:
        higher, lower = max(higher, lower), min(higher, lower)  # get the maximum and minimum numbers
        higher, lower = lower, higher % lower  # reassign the accordingly
        if lower == 0:  # if we have gotten the gcf break the loop and return it
            break
    return higher


if __name__ == '__main__':
    print(gcf(17, 90))
