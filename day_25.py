from typing import Union, List, Tuple, Set
from string import ascii_uppercase, ascii_lowercase
from random import choice, shuffle


def binary_search(item: str, iterable: Union[List, Tuple, Set]) -> int:
    """
    Implementation of the binary search algorithm (https://en.wikipedia.org/wiki/Binary_search_algorithm)
    :param iterable:the object to be searched. Allowed types are list, tuples or sets
    :param item:the item to be searched for. Must be of type int and sorted ascendingly for function to work properly
    :return:the index of the item if it is contained in the list, else -1
    """
    assert any((isinstance(iterable, list), isinstance(iterable, set),
                isinstance(iterable, tuple))), f'Expected a class list, tuple or set for parameter iterable, you pass' \
                                               f' in a {iterable.__class__}'
    assert all(isinstance(x, str) for x in item), f"All item of the iterable must be of type string"
    if iterable != sorted(iterable):
        print('WARNING: ITERABLE NOT SORTED ASCENDINGLY')
    lowest: int = 0  # the first item index
    highest: int = len(iterable) - 1  # the last item index
    while highest >= lowest:  # while we haven't searched the entire string
        middle: int = (highest + lowest) // 2  # get the middle index
        if iterable[middle] == item:  # if the item at the index is the number return its index
            return middle
        elif iterable[middle] > item:  # else if it is lower shift the higher index to the middle position - 1,
            # cutting the
            # iterable in half
            highest = middle - 1
        else:
            lowest = middle + 1  # if it is higher, shift the lower index to the middle
    return -1  # if the item is not found, return -1


if __name__ == '__main__':
    test = sorted([x for x in ascii_lowercase + ascii_uppercase])
    to_search = choice(test)
    print(f'Found {to_search} at position {binary_search(to_search, test)}')
    shuffle(test)
    print('After shuffling...')
    print(f'Found {to_search} at position {binary_search(to_search, test)}')
