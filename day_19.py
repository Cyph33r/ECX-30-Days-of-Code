from datetime import date


def get_weekday(*, year, month, day):
    """
    Get the day of the week that a particular day of the month falls on
    :param year: the year
    :param month: the month
    :param day: the day
    """
    assert isinstance(year, int) and isinstance(year, int) and isinstance(year,
                                                                          int), "All parameters must be of class int"
    today = date(year, month, day)
    print(today.weekday())


if __name__ == '__main__':
    get_weekday(year=2001, month=8, day=90)
