from string import punctuation


def count_chars(sentence: str) -> dict[str, int]:
    """
    Counts the characters in a string. This function is case agnostic so 'f' and 'F' would be treated as the character
    :param sentence: the sentence to be counted
    :return: A dictionary object containing a mapping of all characters in the sentence to their respective counts as
integers
    """
    assert isinstance(sentence,
                      str), f'Expected one parameter of class str, you pass in a {sentence.__class__}'  # sanitise input
    char_count = dict()  # character count
    for char in sentence:  # get each character in the string
        char = char.lower()
        if char in char_count.keys():  # if it exists in the dictionary add 1 to its count/value
            char_count[char] += 1
        else:
            char_count.update({char: 1})  # else add the character with a count/value of 1
    return char_count


def count_words(sentence: str) -> dict[str, int]:
    """
    Counts the characters in a string. This function is case agnostic so 'if' and 'IF' or 'iF' would be treated as
    the word
    :param sentence: the sentence to be counted
    :return: A dictionary object containing a mapping of all words in the sentence to their respective counts as ints
    """
    assert isinstance(sentence,
                      str), f'Expected one parameter of class str, you pass in a {sentence.__class__}'  # sanitise input
    word_count = dict()  # word count
    for word in sentence.split():  # get each word in the string
        word = word.strip(punctuation).lower()  # remove any punctuations at the ends
        if word in word_count.keys():  # if word exists in the dictionary add 1 to the count/value
            word_count[word] += 1
        else:
            word_count.update({word: 1})  # else create it with a count/value of 1
    return word_count


if __name__ == '__main__':
    print(count_chars('It is good!'))
    print(count_words('It is not good!'))
