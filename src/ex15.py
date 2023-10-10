"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    index = 0
    num_list.sort()
    if num_list.__len__() == 0:
        return None
    else:
        index = num_list.__len__() // 2
        if num_list.__len__() %2 == 0:
            return 0.5 * (num_list[index] + num_list[index - 1])
        else:
            return num_list[index]

