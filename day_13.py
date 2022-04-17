from re import findall, ASCII
from typing import List


def get_acronyms(sentence: str) -> List[str]:
    """
    Finds the list of all the acronyms in a given string provided by sentence
    :param sentence: The string you want to search for acronyms
    :return: A list of string containing all the acronyms in sentence
    """
    assert isinstance(sentence,
                      str), f"This function only takes in a parameter of class str you passed in a {sentence.__class__}"
    matched = findall(r'\b[A-Z]{2,}\b', sentence, flags=ASCII)  # find all acronyms using regex
    return matched  # return the matched acronyms as a list


if __name__ == '__main__':
    print(get_acronyms('SMH. The NPF is really a joke'))
