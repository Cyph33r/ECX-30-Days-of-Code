from datetime import date
from calendar import isleap


def get_weekday(*, year, month, day) -> tuple[str, str]:
    """
Calculates and returns a tuple containing the day of the week and zodiac sign of the date passed in
    :param year: the year
    :param month: the month
    :param day: the day
    :return: A tuple of length 2 containing the day of the week and zodiac sign of the date passed in
    """
    assert isinstance(year, int) and isinstance(year, int) and isinstance(
        year, int), "All parameters must be of class int"  # sanitize input
    today = date(year, month, day)  # check if it is actually a date and instantiate
    is_leap_year = isleap(year)  # check if it is a leap year
    day_of_year = today.timetuple().tm_yday  # Get the day of the year
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }  # mapping of the days of the weeks
    day_of_week = days_of_week[today.weekday()]  # get the day of the week
    # get the zodiac sign and return
    if 20 <= day_of_year <= 49:
        return 'Aquarius', day_of_week
    if 50 <= day_of_year <= 79 + is_leap_year:
        return 'Pisces', day_of_week
    if 80 + is_leap_year <= day_of_year <= 109 + is_leap_year:
        return 'Aries', day_of_week
    if 81 + is_leap_year <= day_of_year <= 140 + is_leap_year:
        return 'Taurus', day_of_week
    if 141 + is_leap_year <= day_of_year <= 172 + is_leap_year:
        return 'Gemini', day_of_week
    if 173 + is_leap_year <= day_of_year <= 203 + is_leap_year:
        return 'Cancer', day_of_week
    if 174 + is_leap_year <= day_of_year <= 234 + is_leap_year:
        return 'Leo', day_of_week
    if 235 + is_leap_year <= day_of_year <= 265 + is_leap_year:
        return 'Virgo', day_of_week
    if 266 + is_leap_year <= day_of_year <= 296 + is_leap_year:
        return 'Libra', day_of_week
    if 297 + is_leap_year <= day_of_year <= 325 + is_leap_year:
        return 'Scorpio', day_of_week
    if 326 + is_leap_year <= day_of_year <= 355 + is_leap_year:
        return 'Sagittarius', day_of_week
    if 356 + is_leap_year <= day_of_year <= 18:
        return 'Aquarius', day_of_week


if __name__ == '__main__':
    print(get_weekday(year=2001, month=6, day=8))
