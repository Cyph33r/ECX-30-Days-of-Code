def get_palindromes(num):
    num_str = str(num)  # convert the number to a string for easy manipulation
    num_len = len(num_str)
    first_half = num_str[0:num_len // 2]  # get the first half of the string
    palindromes = []
    for i in range(0, int(first_half) + 1):  # iterate from 0 to the first half
        formatted = str(i).zfill(num_len // 2)  # fill it with zeros, so it would be of the appropriate length
        palindrome = []
        if num_len % 2 == 0:  # if the number has even digits...
            palindrome = [formatted + formatted[::-1]]  # take on half, mirror it and join it back
        else:  # if it is odd...
            for j in range(10):  # take the two mirrored halves and them to the various possibilities of the middle
                # number(0 - 9)
                palindrome.append(formatted + str(j) + formatted[::-1])
        if int(palindrome[0]) > num:
            break
        palindromes += palindrome

    print(f"{len(palindromes)} palindrome(s) found")
    return sorted(palindromes)


print(get_palindromes(5506))
