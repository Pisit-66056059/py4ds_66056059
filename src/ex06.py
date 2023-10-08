"""
Exercise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # Fix : complete this
    if (num >= 10) & (num < 20):
        return f'{num}th'
    else:
        if num % 10 == 0:
            return f'{num}th'
        elif num % 10 == 1:
            return f'{num}st'
        elif num % 10 == 2:
            return f'{num}nd'
        elif num % 10 == 3:
            return f'{num}rd'
        else:
            return f'{num}th'
