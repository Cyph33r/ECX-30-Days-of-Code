def escape_the_well(metres):
    assert isinstance(metres, int) or isinstance(metres,
                                                 float), f"functions only takes number but you entered a {metres.__class__} "
    distance = 0  # distance of the man from the bottom of the well
    days_passed = 0
    while True:
        days_passed += 1  # increment the numbers of day_passed after an entire day
        distance += 5  # distanced travelled by the man at the end of an entire day i.e 8 - 3
        if distance + 3 >= metres:  # check if the man escaped before the night fell
            break
    print(f"The man escaped on day {days_passed}")


if __name__ == '__main__':
    escape_the_well(17)
