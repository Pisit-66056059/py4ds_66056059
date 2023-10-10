"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    mode_count = 0
    number = 0
    if num_list.__len__() == 0:
        return None
    else:
        for x in num_list:
            count_x = num_list.count(x)
            if count_x > mode_count:
                mode_count = count_x
                number = x
    return number