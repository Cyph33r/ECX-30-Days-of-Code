from datetime import date


def get_weekday(*, year, month, day):
    """
    Get the day of the week that a particular day of the month falls on
    :param year: the year
    :param month: the month
    :param day: the day
    """
    assert isinstance(year, int) and isinstance(year, int) and isinstance(
        year, int), "All parameters must be of class int"
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    today = date(year, month, day)
    return days_of_week[today.weekday()]


if __name__ == '__main__':
    print(get_weekday(year=2001, month=8, day=9))
