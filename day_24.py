import sys
from typing import Union, List, Tuple


def bubble_sort(to_sort: Union[List, Tuple], asc: bool = True):
    """
    Python implementation of the bubble sort algorithm. http://en.wikipedia.com/wiki/bubble_sort.
    :param to_sort:Structure to be sorted.Allowed types are list and tuples
    :param asc: If True, returned list will be in ascending order else it would be descending
    :return: A list sorted according to asc
    """

    def swap(from_index: int, to_index: int):
        try:
            to_sort[from_index], to_sort[to_index] = to_sort[to_index], to_sort[from_index]
        except IndexError as e:
            sys.stderr.write(str(e.with_traceback(None)))

    assert isinstance(to_sort, list) or isinstance(to_sort,
                                                   tuple), f'Expected one parameter of class list or tuple, you pass ' \
                                                           f'in a {to_sort.__class__}'  # sanitise input
    assert all(
        isinstance(x, int) or isinstance(x, float) for x in to_sort), 'Expected an list or tuple of ints or float'

    to_sort = list(to_sort[:])  # copy the list or tuple to avoid mutating the parameter object
    for i in range(0, len(to_sort)):  # for each item in the list
        for j in range(0, len(to_sort) - 1 - i):
            if to_sort[j] > to_sort[j + 1] and asc:  # find the largest element and move it to the bottom
                swap(j, j + 1)
            elif to_sort[j] < to_sort[j + 1] and not asc:  # find the smallest element and move it to the bottom
                swap(j, j + 1)
        print(to_sort)
        input()
    return to_sort  # return a sorted copy


if __name__ == '__main__':
    print(bubble_sort([3, 2, 33, 6, 34, 56, 7, 56, 57, 67, 8, 2, 34, 55, 7569, 2452, 442, 76, 7836, 23]))
