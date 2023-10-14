"""
Exercise 14
"""


def average(num_list: list) -> None:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    total = 0
    if num_list.__len__() == 0:
        return None
    else:
        for x in num_list:
            total = total + x
    return total/num_list.__len__()


