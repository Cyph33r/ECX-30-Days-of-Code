def a_function_that_takes_in_a_list(_list):
    found_items = []  # duplicates that have been found so far
    new_list = []  # new list to be returned
    for item in _list:
        if _list.count(item) > 1:  # check if the item is a duplicate
            if item in found_items:  # check if the item has already been added
                continue
        found_items.append(item)  # add the new item and update the new list
        new_list.append(item)
    return new_list


if __name__ == '__main__':
    print(a_function_that_takes_in_a_list(["a", "b", "a", "a", 3, 3, 2, "hello", "b"]))
