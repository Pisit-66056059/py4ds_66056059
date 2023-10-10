"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    total = []
    if num_list.__len__ == 0:
        return 0
    else:
        for x in num_list:
            total.append(x)
    return sum(total)

def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    total = 1
    if num_list.__len__() == 0:
        return 1
    else:
        for x in num_list:
            total = total * x
    return total

