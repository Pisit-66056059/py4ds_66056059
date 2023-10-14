"""
Exercise 21 : Validate Date
"""


def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    from src.ex20 import is_leap_year
    # Fix : complete this
    if month <= 0 or month > 12:
        return False
    if is_leap_year(year) and (day == 29 and month == 2):
        return True
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day < 32):
        return False
    elif month in (4, 6, 9, 11) and not (1 <= day < 31):
        return False
    elif (month == 2) and not (0 <= day < 29):
        return False
    return True
