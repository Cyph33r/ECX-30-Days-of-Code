def a_function_that_takes_a_list(_list):
    assert isinstance(_list, list) or isinstance(_list,
                                                 tuple), f"This function only takes in a list or a tuple. You passed " \
                                                         f"an object of {_list.__class__} "
    assert len(_list) != 0, "Zero length iterable not allowed"

    max_count = 0  # entry with the highest count
    modal_entry = []
    for entry in set(_list):  # convert the list to a set and iterate
        count = _list.count(entry)
        if count >= max_count:
            if count > max_count:  # if the current entry has the highest count clear the list
                modal_entry.clear()
            max_count = count
            modal_entry.append(entry)  # else if just add the entry
    if len(modal_entry) == 1:
        print(f'The entry with the highest occurrence is {modal_entry[0]}')
    else:
        print(f'The entries with the highest occurrence are {modal_entry}')


if __name__ == '__main__':
    a_function_that_takes_a_list([1, 2, 3, 4, 3, 3, 4, 4, 5, 5, 5])