def check_magic_square(magic_square: list):
    checks = [
        # [[0, 1], [1, 1], [2, 1]],  # centre vertical. hardcoded below
        [[1, 0], [1, 1], [1, 2]],  # centre horizontal
        [[2, 0], [1, 1], [0, 2]],  # upward right diagonal
        [[2, 2], [1, 1], [0, 0]],  # upward left diagonal
        [[0, 0], [0, 1], [0, 2]],  # top horizontal
        [[0, 0], [1, 0], [2, 0]],  # first vertical
        [[2, 0], [2, 1], [2, 2]],  # bottom horizontal
        [[2, 2], [1, 2], [0, 2]]  # last vertical
    ]
    magic_num = sum(
        [magic_square[0][1], magic_square[1][1], magic_square[2][1]])  # make the first check to find the magic num
    for check in checks:
        _sum = 0
        for group in check:
            _sum += magic_square[group[0]][group[1]]  # add the currently checked line to the sum
        if magic_num != _sum:  # if it is not equals to the magic sum, the square is not magical ^_~
            print("This list is not a perfect square ❌❌")
            exit(0)
    print("You entered a magic square ✅✅")  # if the loop completes completely then the list is magical


if __name__ == '__main__':
    test_square = [[2, 7, 6],
                   [9, 5, 1],
                   [4, 3, 8]]
    check_magic_square(test_square)
