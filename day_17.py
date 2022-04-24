def pascals_triangle(height: int):
    """
    Print a Pascal's Triangle of height, height
    :param height:The height of the Pascal's Triangle
    """
    assert isinstance(height,
                      int), f'Expected one parameter of class int, you pass in a {height.__class__}'  # sanitise input
    assert height > 0, f'Expected a positive integer you entered {height}'
    triangle = [[1]]  # hardcoded first row that other rows would be derived from
    for _ in range(0, height - 1):
        to_append = [1]  # first element is always 1
        last_row = triangle[-1]  # get the last row calculated
        for index, num in enumerate(last_row):
            if index < len(last_row) - 1:  # if number has number in front of it calculate sum and append
                to_append.append(num + last_row[index + 1])
            if index == len(last_row) - 1:  # if number is the last append 1
                to_append.append(1)
        triangle.append(to_append)  # add to the pascal triangle

    triangle = list(map(lambda x: " ".join(map(lambda f: str(f), x)), triangle))
    for row in triangle:
        print(row.center(len(triangle[-1])))  # print out the triangle


if __name__ == '__main__':
    pascals_triangle(7)
